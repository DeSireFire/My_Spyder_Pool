import requests

# url = 'https://tu-t1.oss-cn-hangzhou.aliyuncs.com/'
url = 'https://tu-t1.oss-cn-hangzhou.aliyuncs.com/'
H = {
    'Origin':'https://tu.aixinxi.net','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',}

req = requests.post(url=url,headers=H)
print(req.status_code)
print(req.text)
print(req.encoding)
print(req.reason)
print(req.content)
print(req.headers)
