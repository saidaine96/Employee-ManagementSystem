import sqlite3

username = input("Username: ")
password = input("Password: ")

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

cur.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username,password)
)

user = cur.fetchone()

if user:
    print("Login Successful")
else:
    print("Invalid Username or Password")

conn.close()