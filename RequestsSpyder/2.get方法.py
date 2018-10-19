"""
requests库的get()方法与urlopen()方法没有太大的区别，
能达到同样的效果，但是requests库简单得多，
requests.get(url,params,***)
"""
# 首先导入requests
import requests
# 有简入繁，最简单的requests_get爬虫
# req = requests.get(url="http://httpbin.org/get")
# print(req.text)
'''
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.14.2"
  }, 
  "origin": "171.36.8.151", 
  "url": "http://httpbin.org/get"
}
'''


# 再来魔改一下，通过get请求传递参数
# req = requests.get(url="http://httpbin.org/get?name=666&value=888")
# print(req.text)
'''
对比以后可以看到，在args字段这里传参数了！
{
  "args": {
    "name": "666", 
    "value": "888"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.14.2"
  }, 
  "origin": "171.36.8.151", 
  "url": "http://httpbin.org/get?name=666&value=888"
}
'''

# 再人性化一点
data = {
    "name": "666",
    "value": "888",
}
req = requests.get(url="http://httpbin.org/get",params=data)
print(req.text)
print(type(req.text))
print(req.json())
print(type(req.json()))
'''
与之前的结果并没有不同，但是回想一下以前用urllib的时候，就会有些感慨。
不用你再转换什么byte了呢！也不用urllib.parse()方法了！
直接就用！是不是很方便呀！
{
  "args": {
    "name": "666", 
    "value": "888"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.14.2"
  }, 
  "origin": "171.36.8.151", 
  "url": "http://httpbin.org/get?name=666&value=888"
}

<class 'str'>
{'args': {'name': '666', 'value': '888'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.14.2'}, 'origin': '171.36.8.151', 'url': 'http://httpbin.org/get?name=666&value=888'}
<class 'dict'>
通过观察可知，网页内容返回的是str类型，但却是Json格式的（即：{"XX":"XXXX",}的格式），
在这里就可以将返回内容直接解析，从而得到一个字典格式，在这里使用json()来解析。
如果返回内容格式不是Json格式的（即：{"XX":"XXXX",}的格式），用此方法是没用的。
json()解析出来的结果，类型是dict,也就是字典。
'''
