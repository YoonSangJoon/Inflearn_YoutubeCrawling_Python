from bs4 import BeautifulSoup
import urllib.request as req
import os.path

url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1138063100'
savename = 'C:\\Pythonsource\\Workspace\\Crawling\\section4\\Assignment\\Assignment.xml'

if not os.path.exists(savename):
    req.urlretrieve(url, savename)
    print('경로에 폴더가 없어서 제가 새로 만들었습니다. ^^')

xml = open(savename, 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')

info = {}
for data in soup.find_all('data'):
    hr = data.find('hour').string
    tmpHgh = data.find_all('tmx')
    tmpLow = data.find_all('temp')
    if not (hr in info):
        info[hr] = []
    for tmp_1 in tmpHgh:
        info[hr].append(tmp_1.text)
    for tmp_2 in tmpLow:
        info[hr].append(tmp_2.text)

print(info)

with open('C:\\Pythonsource\\Workspace\\Crawling\\section4\\Assignment\\Assignment.txt', 'wt', encoding='utf-8') as f:
    for hr in info.keys():
        print('시간 :',hr)
        f.write(str(hr) + '\n')
        for n in info[hr]:
            print('\t',n)
            f.write('\t'+str(n)+'\n')