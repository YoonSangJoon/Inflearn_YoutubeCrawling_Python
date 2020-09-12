import sqlite3

conn = sqlite3.connect('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section5\\databases\\sqlite2.db')

c = conn.cursor()

c.execute('SELECT * FROM users')

# 특정 로우 출력
# print(c.fetchone())

# n개 로우 출력
# print(c.fetchmany(size=4))

# 전체 로우 출력
# print(c.fetchall())

# 순회 방법 1
# rows = c.fetchall()
# for row in rows:
#     print('usage1 :', row)

# 순회 방법 2
# for row in c.fetchall():
#     print('usage2 :', row)

# 순회 방법 3
# for row in c.execute('SELECT * FROM users'):
#     print('usage3 :',row)

# 조건 조회 1
# param = (1,)
# c.execute('SELECT * FROM users WHERE id = ?', param)
# print(c.fetchall())

# 조건 조회 2
# param = 1
# c.execute("SELECT * FROM users WHERE id = '%s'" % param)
# print(c.fetchall())

# 조건 조회 3
# c.execute("SELECT * FROM users WHERE id = :Id", {'Id': 1})
# print(c.fetchall())
# print(c.fetchone())

# 조건 조회 4
# param = (1,4)
# c.execute("SELECT * FROM users WHERE id IN (?,?)", param)
# print(c.fetchall())

# 조건 조회 5
# c.execute("SELECT * FROM users WHERE id = :id1 OR id = :id2",{"id1":1, "id2":1})
# print(c.fetchall())

# DUMP
with conn:
    with open('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section5\\data\\test2.dump', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Write Complete!')