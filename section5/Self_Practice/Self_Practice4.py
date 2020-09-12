import sqlite3
import simplejson as json
import datetime

conn = sqlite3.connect('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section5\\databases\\sqlite2.db')

now = datetime.datetime.now()

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

c = conn.cursor()

# c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)')

userList = (
    (3, 'lee', 'lee@naver.com', '010-2222-3333', 'lee.com', nowDatetime),
    (4, 'park', 'park@naver.com', '010-2222-3333', 'park.com', nowDatetime),
    (5, 'joe', 'joe@naver.com', '010-2222-3333', 'joe.com', nowDatetime)
)

# c.executemany('INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)', userList)

with open('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section5\\data\\users.json', 'r') as infile:
    r = json.loads(infile.read())
    userData = []
    for user in r:
        t = (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDatetime)
        userData.append(t)
    c.executemany('INSERT INTO users(id,username,email,phone,website,regdate) VALUES (?,?,?,?,?,?)', userData)

conn.commit()
conn.close()