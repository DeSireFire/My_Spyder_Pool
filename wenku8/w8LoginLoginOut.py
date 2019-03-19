import requests,chardet

w8LoginUrl = 'https://www.wenku8.net/login.php?do=submit&jumpurl=http%3A%2F%2Fwww.wenku8.net%2Findex.php'
w8IndexUrl = 'http://www.wenku8.net/index.php'
w8LoginOutUrl = 'https://www.wenku8.net/logout.php'

w8LoginHeader = {
'content-type':'application/x-www-form-urlencoded',
'origin':'https://www.wenku8.net',
'referer':'https://www.wenku8.net/login.php?jumpurl=http%3A%2F%2Fwww.wenku8.net%2Findex.php',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

w8LoginOutHeader = {
# 'referer':'http://www.wenku8.net/modules/article/packshow.php?id=2528&type=txt',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

w8LoginData = {
'username':'*',
'password':'*',
'usecookie':'0',
# 'usecookie':'315360000',
'action':'login',
'submit':'(unable to decode value)',
}
sessReq = requests.session()

# 登陆
w8Respone = sessReq.post(url=w8LoginUrl,headers=w8LoginHeader,data=w8LoginData)
w8Respone.encoding = chardet.detect(w8Respone.content)['encoding']
if w8Respone.encoding == "GB2312":
    w8Respone.encoding = "GBK"
# print(w8Respone.text)
print(w8Respone.cookies.items())
print(w8Respone.headers)

# 登陆后主页
w8IndexResone = sessReq.get(url=w8IndexUrl)
w8IndexResone.encoding = chardet.detect(w8IndexResone.content)['encoding']
if w8IndexResone.encoding == "GB2312":
    w8IndexResone.encoding = "GBK"
# print(w8IndexResone.text)
print(w8IndexResone.cookies.items())
print(w8IndexResone.headers)
if '退出登录' in w8IndexResone.text:
    print('登陆成功！')
else:
    print('登陆失败！')

# 退出
w8ResponeOut = sessReq.get(url=w8LoginOutUrl)
w8ResponeOut.encoding = chardet.detect(w8ResponeOut.content)['encoding']
if w8ResponeOut.encoding == "GB2312":
    w8ResponeOut.encoding = "GBK"
# print(w8ResponeOut.text)
print(w8ResponeOut.cookies.items())
print(w8ResponeOut.headers)