import sqlite3

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

fname = input("First Name: ")
lname = input("Last Name: ")
username = input("Username: ")
password = input("Password: ")
email = input("Email: ")
mobile = input("Mobile: ")

cur.execute("""
INSERT INTO users
(first_name,last_name,username,password,email,mobile)
VALUES(?,?,?,?,?,?)
""",(fname,lname,username,password,email,mobile))

conn.commit()
conn.close()

print("User Added Successfully")
