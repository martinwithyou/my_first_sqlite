import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test_demo_2.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.execute(r"insert into user values ('A-004', 'Adams', 95)")
cursor.execute(r"insert into user values ('A-005', 'Barts', 62)")
cursor.execute(r"insert into user values ('A-006', 'Lisas', 78)")
cursor.execute(r"insert into user values ('A-007', 'Adamd', 95)")
cursor.execute(r"insert into user values ('A-008', 'Bartd', 62)")
cursor.execute(r"insert into user values ('A-009', 'Lisad', 78)")
cursor.close()
conn.commit()
conn.close()
