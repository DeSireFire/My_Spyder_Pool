import requests,time


url = 'http://shaoq.com:7777/exam'

header = {
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding':'gzip, deflate',
# 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'session=0d6f8232d0aa1941aa483f96496d353d',
'Host':'shaoq.com:7777',
'If-None-Match':'"b0ff84fd9783d259d3b5433e97d90ad9585001c5"',
'Referer':'http://shaoq.com:7777/exam',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'','
}
req = requests.get(url=url,headers=header)
print(req.headers['Date'])
print(req.headers['Etag'])
print(req.headers['Set-Cookie'].split(';')[0])
header['Cookie'] = req.headers['Set-Cookie'].split(';')[0]
header['If-None-Match'] = req.headers['Etag']
del header['Cache-Control']
print(header)
time.sleep(3)
req2 = requests.get(url=url,headers=header)
print(req2.headers['Date'])
print(req2.text)
print(req2.headers['Content-Length'])
# # 查看请求结果的类型
# print(type(req))
# print("*"*50)
# # 通过属性查看请求状态码
# print(req.status_code)
# print("*"*50)
# # 查看请求结果网页内容的类型
# print(type(req.text))
# print("*"*50)
# # 查看请求后获得cookies
# print(type(req.cookies))
# print(req.cookies)
# for i in req.cookies:
#     print(i.name+"="+i.value)
# print("*"*50)
# # 查看请求结果网页内容
# print(req.text)
# print("*"*50)