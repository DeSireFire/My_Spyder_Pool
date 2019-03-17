import requests,chardet

w8LoginUrl = 'https://www.wenku8.net/login.php?do=submit&jumpurl=http%3A%2F%2Fwww.wenku8.net%2Findex.php'
w8IndexUrl = 'http://www.wenku8.net/index.php'
w8LoginOutUrl = 'https://www.wenku8.net/logout.php'

w8LoginHeader = {
'cache-control':'max-age=0',
'content-length':'150',
'content-type':'application/x-www-form-urlencoded',
# 'cookie':'UM_distinctid=1695d3e13ed303-0fafa8e5319d4e-8383268-144000-1695d3e13ef505; Hm_lvt_d72896ddbf8d27c750e3b365ea2fc902=1552047533,1552830955; CNZZDATA4601171=cnzz_eid%3D2101612498-1552047901-https%253A%252F%252Fwww.wenku8.net%252F%26ntime%3D1552827798; Hm_lvt_acfbfe93830e0272a88e1cc73d4d6d0f=1552050016,1552831623; Hm_lpvt_acfbfe93830e0272a88e1cc73d4d6d0f=1552831623; CNZZDATA5351876=cnzz_eid%3D628519785-1552830451-https%253A%252F%252Fwww.wenku8.net%252F%26ntime%3D1552830451; jieqiVisitId=article_articleviews%3D2254%7C1%7C1592%7C1591; CNZZDATA1309966=cnzz_eid%3D933457048-1552046646-%26ntime%3D1552830700; jieqiVisitInfo=jieqiUserLogin%3D1552831747%2CjieqiUserId%3D380601; CNZZDATA5875574=cnzz_eid%3D1813592095-1552827614-%26ntime%3D1552827614; CNZZDATA1259916661=1672006477-1552046323-%7C1552829978; Hm_lpvt_d72896ddbf8d27c750e3b365ea2fc902=1552833933',
'origin':'https://www.wenku8.net',
'referer':'https://www.wenku8.net/login.php?jumpurl=http%3A%2F%2Fwww.wenku8.net%2Findex.php',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

w8LoginOutHeader = {
'referer':'http://www.wenku8.net/modules/article/packshow.php?id=2528&type=txt',
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
print(w8Respone.text)
print(w8Respone.cookies.items())
print(w8Respone.headers)

# 登陆后主页
w8IndexResone = sessReq.get(url=w8IndexUrl)
w8IndexResone.encoding = chardet.detect(w8IndexResone.content)['encoding']
if w8IndexResone.encoding == "GB2312":
    w8IndexResone.encoding = "GBK"
print(w8IndexResone.text)
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
print(w8ResponeOut.text)
print(w8ResponeOut.cookies.items())
print(w8ResponeOut.headers)