from tinydb import TinyDB
import simplejson as json

db = TinyDB('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section5\\databases\\database1.db')
db2 = TinyDB('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section5\\databases\\database2.db')

albums = db.table('albums')
comments = db.table('comments')

photos = db2.table('photos')
posts = db2.table('posts')

# with open('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section5\\data\\albums.json') as infile:
#     r = json.loads(infile.read())
#     for p in r:
#         albums.insert(p)
#
# with open('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section5\\data\\comments.json') as infile:
#     r = json.loads(infile.read())
#     for p in r:
#         comments.insert(p)
#
# with open('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section5\\data\\photos.json') as infile:
#     r = json.loads(infile.read())
#     for p in r:
#         photos.insert(p)
#
# with open('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section5\\data\\posts.json') as infile:
#     r = json.loads(infile.read())
#     for p in r:
#         posts.insert(p)

# print(albums.all())
# print(comments.all())
#
# print(photos.all())
# print(posts.all())

for item in photos:
    print(item['title'])