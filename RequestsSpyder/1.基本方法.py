"""
urllib是手枪的话，那么现在可以做个升级，玩自动突击步枪了！
urllib开发爬虫相对来说比较繁琐，其中确实有不方便的地方。
为了更方便的开发来实现一些高级操作，就有了更为强大的库requests
现在就来初步体验一下！
"""
# 首先导入requests
import requests

# 发送请求
req = requests.get("https://sm.ms/")
# 查看请求结果的类型
print(type(req))
print("*"*50)
# 通过属性查看请求状态码
print(req.status_code)
print("*"*50)
# 查看请求结果网页内容的类型
print(type(req.text))
print("*"*50)
# 查看请求后获得cookies
print(type(req.cookies))
print(req.cookies)
for i in req.cookies:
    print(i.name+"="+i.value)
print("*"*50)
# 查看请求结果网页内容
print(req.text)
print("*"*50)
# 查看requests.get方法的所有参数
import inspect
print(inspect.getfullargspec(requests.get))

"""
可以发现，requests库对于请求得到的网页内容，在查看的时候要比urllib更加方便。
不再需要类似“.read()”啊，“。decode()”解码啊，还有opener处理cookies之类那么麻烦。
在requests库都能一步到位，而且可以很直观地通过requests.get()看出，这是以get方式发送请求！
除此之外，还有其他几种请求方式：
req = requests.post("http://httpbin.org/post")
req = requests.put("http://httpbin.org/put")
req = requests.delete("http://httpbin.org/delete")
req = requests.head("http://httpbin.org/head")
req = requests.options("http://httpbin.org/options")
"""


