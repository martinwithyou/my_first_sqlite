import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test_demo_3.db')
# if os.path.isfile(db_file):
#     # os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
# cursor.execute('create table stuff(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into stuff values ('A-0032', 'Adam', 95)")
cursor.execute(r"insert into stuff values ('A-0033', 'Bart', 62)")
cursor.execute(r"insert into stuff values ('A-0034', 'Lisa', 78)")

cursor.close()
conn.commit()
conn.close()