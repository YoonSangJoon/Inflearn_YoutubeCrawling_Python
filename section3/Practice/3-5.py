from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

#요청 URL
URL = 'https://www.wishket.com/accounts/login/'

# fake user agent 생성
ua = UserAgent()
with requests.Session() as s:
    s.get(URL)
    LOGIN_INFO = {
        'identification': 'yundosa2',
        'password': 'asb12865!@',
        'csrfmiddlewaretoken': s.cookies['csrftoken']
    }
    # print('headers',s.headers)
    # print('token',s.cookies['csrftoken'])
    # 요청
    response = s.post(URL,data=LOGIN_INFO,headers={'User-Agent':str(ua.chrome),'Referer': 'https://www.wishket.com/accounts/login/'})
    # print('response',response.text)
    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text,'html.parser')
        projectList = soup.select('body > div.gaia > div > div.mb60.container > div.content > div.right-side > div.mb16.user-info.user-info-client > div.user-project')
        for i in projectList:
            print(i.find('div').text)