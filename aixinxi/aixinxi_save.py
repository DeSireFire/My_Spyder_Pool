import requests

H = {
# 'cookie':'PHPSESSID=gb9b12bgkn4a8gv1mf2ur50ud3',
'cookie':'PHPSESSID=qbi4ebphmm6nrmtg6420prs4n1',
'origin':'https://tu.aixinxi.net',
'referer':'https://tu.aixinxi.net/index.php',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
data = {
# 'ming':'o_1cqs8t6tg1s0h1sddovn50ika.mp4',
}
url = 'https://tu.aixinxi.net/includes/save.php'
# url = 'http://httpbin.org/post'


req = requests.post(url=url,headers=H,data=data)
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
