import requests

url = 'https://tu.aixinxi.net/includes/save.php'
# url = 'http://httpbin.org/post'


req = requests.post(url=url,headers=H,data=data)
print(req.status_code)
print(req.text)
print(req.encoding)
print(req.reason)
print(req.content)
print(req.headers)
