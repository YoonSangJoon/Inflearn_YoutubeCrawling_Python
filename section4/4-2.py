from bs4 import BeautifulSoup
import urllib.request as req
import os.path

# url 다운로드
url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
savename = 'C:\\Pythonsource\\Workspace\\Crawling\\section4\\xml\\forcast.xml'

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# Beautifulsoap 파싱
xml = open(savename, 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')

# 지역확인
info = {}
for location in soup.find_all('location'):  # xml에서는 태그들이 이미 정의되어있기 때문에 find 함수가 매우 유용
    loc = location.find('city').string
    # print(loc)
    weather = location.find_all('tmn')
    # print(weather)
    if not (loc in info):
        info[loc] = []
        # 중복확인
    for tmn in weather:
        info[loc].append(tmn.string)

# print(info)
# print(sorted(info.keys()))
# print(list(info.keys()))
# print(info.values())
# key 값 : 좌측
# value 값 : 우측

# 각 지역별 날씨 텍스트 쓰기
with open('C:\\Pythonsource\\Workspace\\Crawling\\section4\\xml\\forcast.txt', 'wt', encoding='utf-8') as f:
    for loc in sorted(info.keys()):
        print('+',loc)
        f.write(str(loc) + '\n')
        for n in info[loc]:
            # n in info[loc] : 각 loc의 values 값 즉, 각 도시의 기온 값
            print('-',n)
            f.write('\t'+str(n)+'\n')
            # \t : 들여쓰기
            # \n : 줄바꿈