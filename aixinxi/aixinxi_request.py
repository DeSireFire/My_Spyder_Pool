import requests


url = 'https://tu-t1.oss-cn-hangzhou.aliyuncs.com/'

files = {'file': open('1.jpg', 'rb')}

req = requests.post(url=url,headers=H,data=data,files=files)
print(req.status_code)
print(req.text)
print(req.encoding)
print(req.reason)
print(req.content)
print(req.headers)
