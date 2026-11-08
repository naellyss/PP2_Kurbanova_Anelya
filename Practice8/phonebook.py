import os
from connect import connect


def init_db():
    conn = connect()
    cur = conn.cursor()

    base_dir = os.path.dirname(__file__)
    with open(os.path.join(base_dir, "functions.sql"), "r", encoding="utf-8") as f:
        cur.execute(f.read())
    with open(os.path.join(base_dir, "procedures.sql"), "r", encoding="utf-8") as f:
        cur.execute(f.read())

    conn.commit()
    cur.close()
    conn.close()


# 1. Search by pattern
def search_by_pattern():
    pattern = input("Enter pattern: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_by_pattern(%s);", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


# 2. Insert or update user
def upsert_user():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
    conn.commit()
    print("Contact saved.")

    cur.close()
    conn.close()


# 3. Insert many users
def insert_many_users():
    n = int(input("How many contacts to add: "))
    names = []
    phones = []

    for _ in range(n):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        names.append(name)
        phones.append(phone)

    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_many_contacts(%s, %s, %s);", (names, phones, []))
    invalid = cur.fetchone()[0]
    conn.commit()

    if invalid:
        print("Incorrect data:", invalid)
    else:
        print("All contacts added.")

    cur.close()
    conn.close()


# 4. Paginated query
def get_paginated():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


# 5. Delete by username or phone
def remove_contact():
    value = input("Enter name or phone to delete: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_contact(%s);", (value,))
    conn.commit()
    print("Contact deleted.")

    cur.close()
    conn.close()


init_db()

while True:
    print("\n1. Search  2. Upsert  3. Add many  4. Pagination  5. Delete  0. Exit")
    cmd = input("Action: ")

    if cmd == "1":
        search_by_pattern()
    elif cmd == "2":
        upsert_user()
    elif cmd == "3":
        insert_many_users()
    elif cmd == "4":
        get_paginated()
    elif cmd == "5":
        remove_contact()
    elif cmd == "0":
        break
