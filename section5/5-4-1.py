import pymysql
import simplejson as json
import datetime

# MySQL Connection
conn = pymysql.connect(host = 'localhost', user = 'python', password = '1111!', db = 'python_app1', charset = 'utf8')

# pyMysql 버전확인
# print('pymysql.version', pymysql.__version__)

# 데이터베이스 선택
conn.select_db('python_app1')

# Cursor 연결
c = conn.cursor()
# print(type(c))

# 데이터베이스 생성
# c.execute('create database python_app2') # DML, DDL, DCL

# 커서 반환
# c.close()

# 접속 해제
# conn.close()

# 트랜잭션 시작 선언
# conn.begin()

# 커밋
# conn.commit()

# 롤백
# conn.rollback()

# 날짜 생성
now = datetime.datetime.now()
nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
# print('nowDateTime :',nowDateTime)

c.execute("CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL, \
            username varchar(20),\
            email varchar(30), \
            phone varchar(30), \
            website varchar(30), \
            regdate varchar(20) NOT NULL, PRIMARY KEY(id))")

# AUTO_INCREMENT, DEFAULT

try:
    with conn.cursor() as c:
        # JSON to MySQL
        with open('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section5\\data\\users.json', 'r') as infile:
            r = json.load(infile)
            userData = []
            for user in r:
                t = (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDateTime)
                userData.append(t)
            c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (%s, %s, %s, %s, %s, %s)", userData)
        conn.commit()
finally:
    conn.close()