import sqlite3

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    username TEXT UNIQUE,
    password TEXT,
    email TEXT,
    mobile TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS department(
    dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_name TEXT,
    description TEXT,
    status INTEGER
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")