import os
from connect import connect


def setup_database():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(25) NOT NULL UNIQUE
        );
    """)

    base_dir = os.path.dirname(__file__)
    for sql_file in ("functions.sql", "procedures.sql"):
        filepath = os.path.join(base_dir, sql_file)
        with open(filepath, "r", encoding="utf-8") as f:
            cur.execute(f.read())

    conn.commit()
    cur.close()
    conn.close()


# 1. Search contacts by pattern (function)
def search_by_pattern():
    pattern = input("Enter search pattern (name or phone): ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_by_pattern(%s);", (pattern,))
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No matching contacts found.")

    cur.close()
    conn.close()


# 2. Insert or update contact (procedure)
def upsert_user():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
    conn.commit()
    print("Contact inserted/updated successfully.")

    cur.close()
    conn.close()


# 3. Bulk insert contacts with phone validation (procedure)
def insert_many_users():
    print("Enter contacts (name,phone) one per line. Press Enter on empty line to finish:")
    names = []
    phones = []

    while True:
        line = input("> ").strip()
        if not line:
            break
        if "," in line:
            name, phone = line.split(",", 1)
            names.append(name.strip())
            phones.append(phone.strip())
        else:
            print("Format must be: name,phone")

    if not names:
        print("No contacts provided.")
        return

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "CALL insert_many_contacts(%s::varchar[], %s::varchar[], %s::text[]);",
        (names, phones, [])
    )
    result = cur.fetchone()
    conn.commit()

    invalid_data = result[0] if result else []
    print("Bulk operation completed.")
    if invalid_data:
        print("Incorrect data (not inserted):")
        for item in invalid_data:
            print(" -", item)
    else:
        print("All contacts had valid phone numbers.")

    cur.close()
    conn.close()


# 4. Query contacts with pagination (function)
def query_paginated():
    limit = int(input("Enter LIMIT: "))
    offset = int(input("Enter OFFSET: "))

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts found for this page.")

    cur.close()
    conn.close()


# 5. Delete contact by username or phone (procedure)
def remove_contact():
    value = input("Enter username or phone to delete: ").strip()

    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_contact(%s);", (value,))
    conn.commit()
    print("Delete procedure executed.")

    cur.close()
    conn.close()


if __name__ == "__main__":
    setup_database()

    while True:
        print("\n1. Search by pattern  2. Upsert contact  3. Bulk insert  4. Paginated view  5. Delete  0. Exit")
        cmd = input("Action: ").strip()

        if cmd == "1":
            search_by_pattern()
        elif cmd == "2":
            upsert_user()
        elif cmd == "3":
            insert_many_users()
        elif cmd == "4":
            query_paginated()
        elif cmd == "5":
            remove_contact()
        elif cmd == "0":
            break
