import urllib.request
import urllib.parse
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API = "https://ssl.pstatic.net/tveta/libs/1285/1285288/243bc5b2fdb208a7bc26_20200519111013568.jpg"

values = {
    'format': 'json'
}
print('before',values)
params = urllib.parse.urlencode(values)
print('after',params)
#요청 URL 생성
url = API + "?" + params
print("요청 url=", url)
#읽기
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
