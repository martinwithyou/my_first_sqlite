import sqlite3

conn = sqlite3.connect('test_demo_3.db')
cursor = conn.cursor()
cursor.execute( 'select * from stuff' )
values = cursor.fetchall()
print(values)
cursor.close()
conn.commit()
conn.close()

