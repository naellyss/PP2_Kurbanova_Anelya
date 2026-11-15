import csv
import json
import os
from connect import connect


def init_db():
    conn = connect()
    if conn is None:
        return
    cur = conn.cursor()
    base_dir = os.path.dirname(__file__)

    with open(os.path.join(base_dir, "schema.sql"), "r", encoding="utf-8") as f:
        cur.execute(f.read())
    with open(os.path.join(base_dir, "procedures.sql"), "r", encoding="utf-8") as f:
        cur.execute(f.read())

    conn.commit()
    cur.close()
    conn.close()


def print_contacts(rows):
    if not rows:
        print("No contacts found.")
        return
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Email: {row[2]} | Birthday: {row[3]} | Group: {row[4]} | Phones: {row[5]}")


# 1. Filter by group
def filter_by_group():
    group_name = input("Enter group (Family / Work / Friend / Other): ").strip()
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name,
               COALESCE(STRING_AGG(p.phone || ' (' || p.type || ')', ', '), 'No phones')
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        WHERE g.name ILIKE %s
        GROUP BY c.id, c.name, c.email, c.birthday, g.name
        ORDER BY c.name;
    """, (group_name,))
    print_contacts(cur.fetchall())
    cur.close()
    conn.close()


# 2. Search by email (partial match)
def search_by_email():
    email_query = input("Enter email pattern (e.g. gmail): ").strip()
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name,
               COALESCE(STRING_AGG(p.phone || ' (' || p.type || ')', ', '), 'No phones')
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        WHERE c.email ILIKE %s
        GROUP BY c.id, c.name, c.email, c.birthday, g.name
        ORDER BY c.name;
    """, (f"%{email_query}%",))
    print_contacts(cur.fetchall())
    cur.close()
    conn.close()


# 3. Sort contacts by name, birthday, or date added
def sort_contacts():
    print("Sort by: 1 - Name  2 - Birthday  3 - Date added")
    choice = input("Choose: ").strip()
    order_map = {
        "1": "c.name ASC",
        "2": "c.birthday ASC NULLS LAST",
        "3": "c.created_at DESC"
    }
    order_clause = order_map.get(choice, "c.name ASC")

    conn = connect()
    cur = conn.cursor()
    cur.execute(f"""
        SELECT c.id, c.name, c.email, c.birthday, g.name,
               COALESCE(STRING_AGG(p.phone || ' (' || p.type || ')', ', '), 'No phones')
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        GROUP BY c.id, c.name, c.email, c.birthday, g.name, c.created_at
        ORDER BY {order_clause};
    """)
    print_contacts(cur.fetchall())
    cur.close()
    conn.close()


# 4. Paginated navigation loop (next / prev / quit)
def paginated_navigation():
    page_size = int(input("Enter page size (e.g. 3): ") or 3)
    offset = 0

    conn = connect()
    cur = conn.cursor()

    while True:
        cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (page_size, offset))
        rows = cur.fetchall()
        page_num = (offset // page_size) + 1
        print(f"\n--- Page {page_num} ---")
        print_contacts(rows)

        cmd = input("\nNavigate [next / prev / quit]: ").strip().lower()
        if cmd == "next":
            if len(rows) < page_size:
                print("Already on the last page.")
            else:
                offset += page_size
        elif cmd == "prev":
            if offset == 0:
                print("Already on the first page.")
            else:
                offset = max(0, offset - page_size)
        elif cmd == "quit":
            break

    cur.close()
    conn.close()


# 5. Export contacts to JSON
def export_to_json(filename="contacts.json"):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        ORDER BY c.id;
    """)
    contacts_rows = cur.fetchall()

    data = []
    for cid, name, email, birthday, group_name in contacts_rows:
        cur.execute("SELECT phone, type FROM phones WHERE contact_id = %s;", (cid,))
        phones = [{"phone": r[0], "type": r[1]} for r in cur.fetchall()]
        data.append({
            "name": name,
            "email": email,
            "birthday": str(birthday) if birthday else None,
            "group": group_name,
            "phones": phones
        })

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    cur.close()
    conn.close()
    print(f"Exported {len(data)} contacts to {filename}.")


# 6. Import contacts from JSON (ask skip or overwrite on duplicate)
def import_from_json(filename="contacts.json"):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if not os.path.exists(filepath):
        print(f"File {filename} not found.")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        contacts_data = json.load(f)

    conn = connect()
    cur = conn.cursor()

    for item in contacts_data:
        name = item.get("name")
        email = item.get("email")
        birthday = item.get("birthday")
        group_name = item.get("group") or "Other"
        phones = item.get("phones", [])

        cur.execute("SELECT id FROM contacts WHERE name = %s;", (name,))
        existing = cur.fetchone()

        if existing:
            action = input(f"Contact '{name}' already exists. [s]kip or [o]verwrite? ").strip().lower()
            if action == "s":
                continue
            contact_id = existing[0]
            cur.execute("CALL move_to_group(%s, %s);", (name, group_name))
            cur.execute(
                "UPDATE contacts SET email = %s, birthday = %s WHERE id = %s;",
                (email, birthday, contact_id)
            )
            cur.execute("DELETE FROM phones WHERE contact_id = %s;", (contact_id,))
        else:
            cur.execute(
                "INSERT INTO contacts (name, email, birthday) VALUES (%s, %s, %s) RETURNING id;",
                (name, email, birthday)
            )
            contact_id = cur.fetchone()[0]
            cur.execute("CALL move_to_group(%s, %s);", (name, group_name))

        for ph in phones:
            cur.execute(
                "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s);",
                (contact_id, ph["phone"], ph.get("type", "mobile"))
            )

    conn.commit()
    cur.close()
    conn.close()
    print("JSON import completed.")


# 7. Extended CSV import (handles email, birthday, group, phone_type)
def import_from_csv(filename="contacts.csv"):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    conn = connect()
    cur = conn.cursor()

    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"].strip()
            phone = row["phone"].strip()
            phone_type = row.get("phone_type", "mobile").strip()
            email = row.get("email", "").strip() or None
            birthday = row.get("birthday", "").strip() or None
            group_name = row.get("group", "Other").strip() or "Other"

            cur.execute("""
                INSERT INTO contacts (name, email, birthday)
                VALUES (%s, %s, %s)
                ON CONFLICT (name) DO UPDATE
                SET email = EXCLUDED.email, birthday = EXCLUDED.birthday;
            """, (name, email, birthday))

            cur.execute("CALL move_to_group(%s, %s);", (name, group_name))
            cur.execute("CALL add_phone(%s, %s, %s);", (name, phone, phone_type))

    conn.commit()
    cur.close()
    conn.close()
    print("Extended CSV contacts imported.")


# 8. Stored procedures & functions calls
def call_add_phone():
    name = input("Enter contact name: ").strip()
    phone = input("Enter new phone: ").strip()
    ptype = input("Enter type (home / work / mobile): ").strip().lower()

    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL add_phone(%s, %s, %s);", (name, phone, ptype))
    conn.commit()
    cur.close()
    conn.close()
    print("Phone added.")


def call_move_to_group():
    name = input("Enter contact name: ").strip()
    group_name = input("Enter target group name: ").strip()

    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL move_to_group(%s, %s);", (name, group_name))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Moved '{name}' to group '{group_name}'.")


def call_search_contacts():
    query = input("Enter search query (name / email / phone / group): ").strip()
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s);", (query,))
    print_contacts(cur.fetchall())
    cur.close()
    conn.close()


if __name__ == "__main__":
    init_db()

    while True:
        print("\n--- TSIS 1: Extended PhoneBook ---")
        print("1. Import extended CSV")
        print("2. Filter by group")
        print("3. Search by email")
        print("4. Sort contacts (name / birthday / date added)")
        print("5. Paginated navigation (next / prev / quit)")
        print("6. Export to JSON")
        print("7. Import from JSON")
        print("8. Add phone to contact (Procedure)")
        print("9. Move contact to group (Procedure)")
        print("10. Multi-field search (Function)")
        print("0. Exit")

        cmd = input("Action: ").strip()

        if cmd == "1":
            import_from_csv()
        elif cmd == "2":
            filter_by_group()
        elif cmd == "3":
            search_by_email()
        elif cmd == "4":
            sort_contacts()
        elif cmd == "5":
            paginated_navigation()
        elif cmd == "6":
            export_to_json()
        elif cmd == "7":
            import_from_json()
        elif cmd == "8":
            call_add_phone()
        elif cmd == "9":
            call_move_to_group()
        elif cmd == "10":
            call_search_contacts()
        elif cmd == "0":
            break
