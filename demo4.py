import sqlite3

conn = sqlite3.connect('test_demo_3.db')
cursor = conn.cursor()

cursor.execute(r"alter table stuff add score int")



cursor.close()
conn.commit()
conn.close()

