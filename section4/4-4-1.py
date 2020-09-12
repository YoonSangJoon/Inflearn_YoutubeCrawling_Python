import simplejson as json

# 딕셔너리(txt) 선언

data = {}
data['people'] = []
data['people'].append({
    'name' : 'kim',
    'website' : 'naver.com',
    'from' : 'Seoul'
})
data['people'].append({
    'name' : 'Park',
    'website' : 'google.com',
    'from' : 'Busan'
})
data['people'].append({
    'name' : 'Lee',
    'website' : 'daum.net',
    'from' : 'Incheon'
})

# print(data)

# Dict (txt) -> str

e = json.dumps(data, indent=4)
# indent : 숫자 만큼 들여쓰기


# print(type(e))
# print(e)

# str -> 딕셔너리(txt)
# d = json.loads(e)
# print(type(d))
# print(d)

# 내용 정렬할 때에는 온라인에서 json sort 사이트 사용.

with open('C:\\Pythonsource\\Workspace\\Crawling\\section4\\txt\\member.json', 'w') as outfile:
    outfile.write(e)

with open('C:\\Pythonsource\\Workspace\\Crawling\\section4\\txt\\member.json', 'r') as infile:
    r = json.loads(infile.read())
    print('===========')
    # print(type(r))
    # print(r)
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')