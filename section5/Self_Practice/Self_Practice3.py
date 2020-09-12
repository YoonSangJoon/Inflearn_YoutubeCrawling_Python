from tinydb import TinyDB, Query

db = TinyDB('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section5\\databases\\database3.db')

db.insert({'name' : 'kim', 'email' : '1@naver.com'})
db.insert_multiple([{'name': 'lee', 'email': 'test2@daum.net'},{'name': 'park', 'email': 'test3@daum.net'}]) #JsonArray 삽입

SQL = Query()

el = db.get(SQL.name == 'kim')

print(el)
print(el.doc_id)

db.upsert({'email' : 'test1@gmail.com', 'login':True}, SQL.name == 'kim')

db.remove(doc_ids = [2,3])
db.remove(SQL.name == 'park')

print(db.all())

db.close()