import simplejson as json

# 딕셔너리(txt) 선언
data = {}
data['people'] = []
data['people'].append({
    'name' : 'kim',
    'website' : 'naver.com',
    'from' : 'Seoul',
    'grade' : [77,89,91,95]
})
data['people'].append({
    'name' : 'Park',
    'website' : 'google.com',
    'from' : 'Busan',
    'grade' : [66,39,71,92]
})
data['people'].append({
    'name' : 'Lee',
    'website' : 'daum.net',
    'from' : 'Incheon',
    'grade' : [71,85,71,35]
})

# json 파일쓰기 (dump)

with open('C:\Pythonsource\Workspace\Crawling\section4\Json\member.json','w') as outfile:
    json.dump(data, outfile)
    # 새로 추가한 grade의 key와 value가 추가됨.

with open('C:\Pythonsource\Workspace\Crawling\section4\Json\member.json','r') as infile:
    r = json.load(infile)
    # print(type(r))
    # print(r)
    print('========================')
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        t = p['grade']
        grade=''
        for g in t:
            grade = grade + str(g)
        print('Grade:',grade.lstrip())
        # lstrip : 왼쪽 공백 제거
        print('')