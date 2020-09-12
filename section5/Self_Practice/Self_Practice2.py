from tinydb import TinyDB, Query, where

db = TinyDB('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section5\\databases\\database1.db')
db2 = TinyDB('C:\\Pythonsource\\Workspace\\Crawling\\Class\\section5\\databases\\database2.db')

albums = db.table('albums')
comments = db.table('comments')

photos = db2.table('photos')
posts = db2.table('posts')

Albums = Query()
Comments = Query()

Photos = Query()
Posts = Query()

album_1 = albums.search(Albums.id == 3)
print('result_a :',albums.search(Albums.id == 3))
print('result_a :',albums.search(Albums['id'] == 3))
print('result_a :',albums.search(where('id') == 3))
print('result_a :',albums.search(Query()['id'] == 3))
print('result_a :',album_1)

print()

comment_1 = comments.search(Comments.id == 3)
print('result_c :',comments.search(Comments.id == 3))
print('result_c :',comments.search(Comments['id'] == 3))
print('result_c :',comments.search(where('id') == 3))
print('result_c :',comments.search(where('id') == 3))
print('result_c :',comments.search(Query()['name'] == "et omnis dolorem"))
print('result_c :',comment_1)

print()

print('matches :',photos.search(Photos.title.matches('rep')))

print()

print('negate :',photos.search(~(Photos.title == 'rep')))

print()

print('or :',photos.search((Photos.title == 'reprehenderit est deserunt velit ipsam') | (Photos.title == 'officia porro iure quia iusto qui ipsa ut modi')))

print()

print('and :',photos.search((Photos.title == 'reprehenderit est deserunt velit ipsam') & (Photos.id == 2)))

print()

print('len :',len(albums))
print('len :',len(comments))
print('len :',len(photos))
print('len :',len(posts))

print()

print('get :',posts.get(Posts.title == 'eum et est occaecati'))
print('contains :',posts.contains(Posts.title == 'eum et est occaecati'))
print('count :',posts.count(Posts.title == 'eum et est occaecati'))

print()

db.close()
db2.close()