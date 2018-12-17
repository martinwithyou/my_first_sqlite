import sqlite3
conn = sqlite3.connect('test2.db')
cursor = conn.cursor()
cursor.execute('select * from user ')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()