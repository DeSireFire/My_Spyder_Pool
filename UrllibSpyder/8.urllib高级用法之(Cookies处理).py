# 这次实现一个简单的验证登陆实例
import urllib.request
import http.cookiejar

# 由简入繁，先来一个的简单实例
myUrl =  "https://www.baidu.com/"
myHeaders = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
}
#
req = urllib.request.Request(url=myUrl,headers=myHeaders)

# 载入cookies处理器
cookie = http.cookiejar.CookieJar()
handler_cookie = urllib.request.HTTPCookieProcessor(cookie)

# 在此处build_opener()方法中放入handler类处理即可。
opener = urllib.request.build_opener(handler_cookie)

response = opener.open(req)
# 遍历打印所获得的cookies
for i in cookie:
    print(i.name+"="+i.value)
print("*"*50)

# 可将请求得到的cookies保存在一个文本文件里（分两种格式）
# 保存为MozillaCookie格式
fileName = "MozillaCookie.txt"
fileCookie = http.cookiejar.MozillaCookieJar(fileName)
handler_fileCookie = urllib.request.HTTPCookieProcessor(fileCookie)
opener = urllib.request.build_opener(handler_fileCookie)
response_MozillaCookie = opener.open(req)
fileCookie.save(ignore_discard=True,ignore_expires=True)

# 保存为LWPCookie格式
fileName = "LWPCookie.txt"
fileCookie = http.cookiejar.LWPCookieJar(fileName)
handler_fileCookie = urllib.request.HTTPCookieProcessor(fileCookie)
opener = urllib.request.build_opener(handler_fileCookie)
response_LWPCookie = opener.open(req)
fileCookie.save(ignore_discard=True,ignore_expires=True)

# 读取文本文件中的cookie来使用
read_cookie = http.cookiejar.LWPCookieJar()
read_cookie.load("LWPCookie.txt",ignore_discard=True,ignore_expires=True)
for i in read_cookie:
    print(i.name+"="+i.value)
print("*"*50)
# 到此可以观察跟前面的是一样的cookie,使用这些cookie便可以实现它们的复用
handler_read_cookie = urllib.request.HTTPCookieProcessor(read_cookie)
opener = urllib.request.build_opener(handler_read_cookie)
response_read_cookie = opener.open(req)
# print(response_read_cookie.read().decode("utf-8"))