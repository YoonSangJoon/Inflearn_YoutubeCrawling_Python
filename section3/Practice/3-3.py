import requests, json

#r = requests.get('https://api.github.com/events')
#r.raise_for_status() # http 에러 메시지 출력
#print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('name','kim',domain='httpbin.org',path='/cookies')

# r = requests.get('http://httpbin.org/cookies',cookies=jar)
# r.raise_for_status()
# print(r.text)

#r = requests.get('http://github.com',timeout=3)
#print(r.text)

#r = requests.post('http://httpbin.org/post',data={'name':'kim'}, cookies=jar)
#print(r.text)

payload1 = {'key1':'value1','key2':'value2'} # dict
payload2 = (('key1','value1'),('key2','value2')) # tuple'
payload3 = {'some':'nice'}


r = requests.post('http://httpbin.org/post', data=payload1)
print(r.text)
r = requests.post('http://httpbin.org/post', data=json.dumps(payload3))
print(r.text)