#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test_demo_7.db')
c = conn.cursor()
print("Opened database successfully")

c.execute("UPDATE COMPANY set SALARY = 144444444444444445000.00 where ID=1")
conn.commit()
print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()