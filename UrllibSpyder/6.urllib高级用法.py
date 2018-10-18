'''
构造请求，终于是让爬虫更加完善了，
但是对于一些高级操作，例如处理cookies,代理等还是不够足的，在这里还可以将urllib爬虫进一步完善
对，你没看错。
Python原生的爬虫模块urllib也同样可以完成cookies操作和设置代理。
这并不是第三方库Request的特色！

在此引入urllib.request的BaseHandler类！BaseHandler，字面意思，基础处理器！
以基础处理器为模板诞生出了更多具体作用的处理器子类，
通过它们，来完成各种各样的高级操作！

继承基础处理器类的常用子例如下：
HTTPDefaultErrorHandler:处理HTTP响应错误，错误都会抛出HTTPError类型的异常。
HTTPHandler:用于处理重定向。
HTTPCookiesProcessor:处理Cookies。
ProxyHandler:设置代理，默认为空
HTTPPasswordMgr:设置管理密码，它维护了用户名和密码的表
HTTPBasicAuthHandler:管理认证，如果某个链接打开需要认证，那么可以用它来解决认证问题

之前说到，如果把urlopen比喻为一把手枪的话，那么现在再来加入一把新武器。
Opener方法，可以完成更加高级的功能,
在这里使用Handler类来构建Opener!
Opener的open()跟urlopen用法几乎一样，就是多了处理这一块。
'''
import urllib.request
import urllib.parse

# 由简入繁，先来一个的简单实例


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

# 在此处build_opener()方法中放入handler类处理结果即可。因为是简单例子，所以此处留空
opener = urllib.request.build_opener()

response = opener.open(req)
print(response.read().decode("utf-8"))
print("*"*50)
'''
可以观察到，出了多了一步“opener = urllib.request.build_opener()”外，open()跟urlopen用法是一样的。可以与之前的urlopen结果进行对比！
返回的运行结果如下：
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "hello": "world!"
  }, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Connection": "close", 
    "Content-Length": "14", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
  }, 
  "json": null, 
  "origin": "171.36.8.151", 
  "url": "http://httpbin.org/post"
}

**************************************************
'''

