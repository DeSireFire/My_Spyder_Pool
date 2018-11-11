import requests

H = {
'Origin':'https://tu.aixinxi.net',
'Referer':'https://tu.aixinxi.net/index.php',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
data = {
'name':'o_test.jpg',
'policy':'eyJleHBpcmF0aW9uIjoiMjAxOC0xMS0xMVQxNDozNzo1NFoiLCJjb25kaXRpb25zIjpbWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsMCwxMDQ4NTc2MF0sWyJzdGFydHMtd2l0aCIsIiRrZXkiLCIiXV19',
'signature':'1UEnB6y1T4boNZzqPtEp5NkXOM0=',
'OSSAccessKeyId':'LTAIyUoGoXRUSdwm',
'key':'o_test.jpg',
'success_action_status':'200',
}
url = 'https://tu-t1.oss-cn-hangzhou.aliyuncs.com/'
# url = 'http://httpbin.org/post'

files = {'file': open('1.jpg', 'rb')}

req = requests.post(url=url,headers=H,data=data,files=files)
print(type(req))
print("*"*50)
# 通过属性查看请求状态码
print(req.status_code)
print("*"*50)
# 查看请求结果网页内容的类型
print(type(req.text))
print(req.text)
print("*"*50)
# 查看请求后获得cookies
print(type(req.cookies))
print(req.cookies)
for i in req.cookies:
    print(i.name+"="+i.value)
print("*"*50)
print(req.encoding)
print(req.reason)
print(req.content)
print(req.headers)
print(req.request)
print(req.history)
print(req.links)
print(req.raw)
print(req.elapsed)
