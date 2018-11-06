'''
urlopen是用来向目标网页发送的方法
Request是用来构造请求的方法

最原始的爬虫通过urlopen就已经初步实现，但是在目前还远远不够。
光靠urlopen的爬虫是不够完整的，很容易被反扒，所以就要借助Request方法，来完善它

如果要做个比喻的话，前者就是手枪，后者就是弹夹
我们需要往“弹夹”中塞入子弹
'''
import urllib.request

# 由简入繁，先来一个有request的简单实例
# req = urllib.request.Request("http://httpbin.org/get")
# response = urllib.request.urlopen(request)
# print(response.read().decode("utf-8"))
# print("*"*50)

'''
urllib.request.Request方法所常用的参数：
url:网页地址
data:附加信息
headers:请求头
method:请求方式（get、post等）
'''
# 使用Request方法装填“子弹”！
import urllib.parse

myUrl =  "http://httpbin.org/post"
myHeaders = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Host":"httpbin.org",
}
mydict = {
    "hello":"world!"
}
myDate = bytes(urllib.parse.urlencode(mydict),encoding="utf-8")

req = urllib.request.Request(url=myUrl,data=myDate,headers=myHeaders,method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
print("*"*50)
