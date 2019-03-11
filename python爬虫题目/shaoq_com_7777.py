import requests
__author__ = 'RaXian'

url = 'http://shaoq.com:7777/exam'
req_s = requests.session()
req = req_s.get(url=url)
print (req.cookies.items())
print (req.text)
for i in range(1, 14):
    try:
        response = req_s.get('http://shaoq.com:7777/img/%s.png'%i, timeout=0.1)
    except:
        pass
req = req_s.get(url=url)
print (req.cookies.items())
print (req.headers)
print (req.text)



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
# print (req.cookies.items())
# for i in req.cookies:
#     print(i.name+"="+i.value)
# print("*"*50)
# # 查看请求结果网页内容
# print(req.text)
# print("*"*50)