import requests
from bs4 import BeautifulSoup

# 로그인 유저정보
LOGIN_INFO = {
    'user_id': 'yundosa2',
    'user_pw': 'asb12865!@'
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:

    login_req = s.post('https://user.ruliweb.com/member/login_proc', data=LOGIN_INFO)
    # HTML 소스 확인
    #print('login_req',login_req.text)
    # HTTP Header 확인
    #print('login_req',login_req.headers)

    # Response 정상 확인
    # 서버 에러코드가 정상이 아닐경우 예외 발생
    if login_req.status_code == 200 and login_req.ok:
        #권한이 필요한 게시판 게시글 가져오기
        post_one = s.get('https://bbs.ruliweb.com/market/board/32/read/4731645?')

        #예외 발생
        post_one.raise_for_status()
        #print(post_one.text)

        #BeautifulSoup 선언
        soup = BeautifulSoup(post_one.text, 'html.parser')
        # print(soup.prettify())

        article = soup.select_one("#board_read > div > div.board_main > div.board_main_view").find_all('span')

        print(article)

        for i in article:
            if i.span is not None and \
                    i.span.string is not None:
                print(i.span.string)
