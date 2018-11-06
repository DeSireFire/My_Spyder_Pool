# 首先就以设置爬虫代理为例
from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
import urllib.request

# 实例中的IP时间久了很可能会失效，可以自己寻找新的来更换
proxy_handler = ProxyHandler({
    # "http":"http://142.154.219.66:43668",
    "http":"http://223.203.0.14:8080",
    # "https":"https://221.7.255.167:80"
    "https":"https://221.7.255.167:80"

})
opener = build_opener(proxy_handler)
try:
    response = opener.open("https://www.iqing.com/")
    print(response.status)
    # print(response.read().decode("utf-8"))
except urllib.error.URLError as ue:
    print(ue.reason)
print("*"*50)

try:
    response = opener.open("https://httpbin.org/get")
    print(response.status)
    # print(response.read().decode("utf-8"))
except urllib.error.URLError as ue:
    print(ue.reason)
print("*"*50)

'''
因为速度非常慢，于是在这里丢出它们的运行结果：
{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/3.6"
  }, 
  "origin": "142.154.219.66", 
  "url": "http://httpbin.org/get"
}

**************************************************
{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/3.6"
  }, 
  "origin": "85.133.185.202", 
  "url": "https://httpbin.org/get"
}

**************************************************

Process finished with exit code 0
可以看出，origin字段的IP发生了变化！
'''