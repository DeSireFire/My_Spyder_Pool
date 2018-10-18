import urllib.request

# 发送请求
response = urllib.request.urlopen("https://tu.aixinxi.net/index.php")
'''
response的类型为http.client.HTTPResponse
这个类型如下几种常用的方法：
read()
readinto()
getheaders()
getheader(name)
fileno()

以及几种常用到的属性：
msg
version
status
reason
debuglevel
closed

'''

# read()方法，读取响应并解码打印
# print(response.read().decode("utf-8"))
# print("*"*50)

# readinfo()方法，暂时未知有何作用
# print(response.readinto())
# print("*"*50)

# getheaders()方法
print(response.getheaders())
print("*"*50)

# getheader(name)方法
print(response.getheader("server"))
print("*"*50)

# fileno()方法，谜一样的数字
print(response.fileno())
print("*"*50)

# msg属性 不知道是什么鬼
print(response.msg)
print("*"*50)

# version属性 不知道是什么鬼版本
print(response.version)
print("*"*50)

# status属性 网页状态码
print(response.status)
print("*"*50)

# reason属性 读取网页是否成功
print(response.reason)
print("*"*50)

# debuglevel属性 不知道是什么鬼
print(response.debuglevel)
print("*"*50)

# closed属性 不知道是什么鬼
print(response.closed)
print("*"*50)