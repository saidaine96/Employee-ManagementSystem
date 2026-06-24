import sqlite3

username = input("Enter Username: ")
new_password = input("Enter New Password: ")

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

cur.execute(
    "UPDATE users SET password=? WHERE username=?",
    (new_password,username)
)

conn.commit()

if cur.rowcount > 0:
    print("Password Reset Successful")
else:
    print("User Not Found")

conn.close()