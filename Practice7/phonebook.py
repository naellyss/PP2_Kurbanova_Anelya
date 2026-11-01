import csv
import os
from connect import connect


# 1. Create table
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(25) NOT NULL UNIQUE
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


# 2. Insert from CSV
def insert_from_csv(filename="contacts.csv"):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    conn = connect()
    cur = conn.cursor()

    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if len(row) >= 2:
                cur.execute(
                    "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING;",
                    (row[0].strip(), row[1].strip())
                )

    conn.commit()
    cur.close()
    conn.close()
    print("CSV contacts added.")


# 3. Insert from console
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING;",
        (name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()
    print("Contact added.")


# 4. Update contact
def update_contact():
    print("1 - Change first name")
    print("2 - Change phone")
    choice = input("Choose: ")

    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        phone = input("Enter current phone: ")
        new_name = input("Enter new name: ")
        cur.execute("UPDATE phonebook SET first_name = %s WHERE phone = %s;", (new_name, phone))
    elif choice == "2":
        name = input("Enter first name: ")
        new_phone = input("Enter new phone: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s;", (new_phone, name))

    conn.commit()
    print("Updated rows:", cur.rowcount)
    cur.close()
    conn.close()


# 5. Query contacts with filters
def query_contacts():
    print("1 - All contacts")
    print("2 - Filter by name")
    print("3 - Filter by phone prefix")
    choice = input("Choose: ")

    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        cur.execute("SELECT * FROM phonebook ORDER BY id;")
    elif choice == "2":
        name = input("Enter name: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s;", (f"%{name}%",))
    elif choice == "3":
        prefix = input("Enter prefix: ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s;", (f"{prefix}%",))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


# 6. Delete contact
def delete_contact():
    print("1 - Delete by username")
    print("2 - Delete by phone")
    choice = input("Choose: ")

    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter username: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s;", (name,))
    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))

    conn.commit()
    print("Deleted rows:", cur.rowcount)
    cur.close()
    conn.close()


create_table()

while True:
    print("\n1. Upload CSV  2. Add contact  3. Update  4. Search  5. Delete  0. Exit")
    cmd = input("Action: ")

    if cmd == "1":
        insert_from_csv()
    elif cmd == "2":
        insert_from_console()
    elif cmd == "3":
        update_contact()
    elif cmd == "4":
        query_contacts()
    elif cmd == "5":
        delete_contact()
    elif cmd == "0":
        break
