import urllib.request
import urllib.parse
import http.cookiejar


aixinxi_login_url = "https://tu.aixinxi.net/includes/userAction.php"
aixinxi_login_url2 = "https://tu.aixinxi.net/index.php"
# aixinxi_login_url = "http://httpbin.org/post"
aixinxi_login_dirt = {
    "action":"login",
    "username":"1025212779@qq.com",
    "password":"RQgannimei233",
}
# 载入cookies处理器
aixinxi_login_cookie = http.cookiejar.CookieJar()
aixinxi_login_handler = urllib.request.HTTPCookieProcessor(aixinxi_login_cookie)
# 在此处build_opener()方法中放入handler类处理即可。
aixinxi_login_opener = urllib.request.build_opener(aixinxi_login_handler)

aixinxi_login_data = bytes(urllib.parse.urlencode(aixinxi_login_dirt),encoding="utf8")
aixinxi_login_request = urllib.request.Request(url=aixinxi_login_url,data=aixinxi_login_data,method="POST")
aixinxi_login_response = aixinxi_login_opener.open(aixinxi_login_request)
# aixinxi_login_
print(aixinxi_login_response.read().decode("utf-8"))
print("*"*50)
for i in aixinxi_login_cookie:
    print(i.name+"="+i.value)
print("*" * 50)
# 使用获取的cookies来的访问网页
handler_read_cookie = urllib.request.HTTPCookieProcessor(aixinxi_login_cookie)
opener2 = urllib.request.build_opener(handler_read_cookie)
response_read_cookie = opener2.open(aixinxi_login_url2)
print("使用获取的cookies来的访问网页成功！")
print("*" * 50)
#上传图片文件
aixinxi_login_url3 = "https://tu.aixinxi.net/includes/save.php"
dirt = {
    "Host":"tu.aixinxi.net",
    "Connection":"keep-alive",
    "Content-Length":"37",
    "Accept":"*/*",
    "Origin":"https://tu.aixinxi.net",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Referer":"https://tu.aixinxi.net/index.php",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
    "ming":"o_1cq3oq991g0q1lt3121t04boka.jpg",
}
aixinxi_login_Images = bytes(urllib.parse.urlencode(dirt),encoding="utf8")
aixinxi_login_request = urllib.request.Request(url=aixinxi_login_url,data=aixinxi_login_data,method="POST")
response_upImages = opener2.open(aixinxi_login_url3)
print(response_upImages.read().decode("utf-8"))
print("*" * 50)