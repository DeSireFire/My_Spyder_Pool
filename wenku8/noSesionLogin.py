'''
在不使用request.session()方法时,实现的wenku8登陆
'''

import requests,chardet,re
from requests.cookies import RequestsCookieJar

textURL = 'http://dl.wenku8.com/packtxt.php?aid=2478&vid=92903&charset=utf-8'
w8LoginUrl = 'https://www.wenku8.net/login.php?do=submit&jumpurl=http%3A%2F%2Fwww.wenku8.net%2Findex.php'
w8IndexUrl = 'http://www.wenku8.net/index.php'
w8LoginOutUrl = 'https://www.wenku8.net/logout.php'

w8LoginHeader = {
'origin':'https://www.wenku8.net',
'referer':'https://www.wenku8.net/login.php?jumpurl=http%3A%2F%2Fwww.wenku8.net%2Findex.php',
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

# sessReq = requests.session()
cookie_jar = RequestsCookieJar()

# 登陆
w8Respone = requests.post(url=w8LoginUrl,headers=w8LoginHeader,data=w8LoginData)
w8Respone.encoding = chardet.detect(w8Respone.content)['encoding']
if w8Respone.encoding == "GB2312":
    w8Respone.encoding = "GBK"
'''
获取登陆请求后服务器响应头所给的'Set-Cookie'键值对,得到如下:
PHPSESSID=jrh3e8u399kgdm5mh63bpibms1v6i6pc; expires=Wed, 20-Mar-2019 13:09:31 GMT; path=/; HttpOnly, PHPSESSID=7idql1ec5qcfo5mijnv717jgmhreidrn; expires=Wed, 20-Mar-2019 13:09:31 GMT; path=/; HttpOnly, jieqiUserInfo=jieqiUserId%3D380601%2CjieqiUserName%3DDeSireFire%2CjieqiUserGroup%3D3%2CjieqiUserVip%3D0%2CjieqiUserName_un%3DDeSireFire%2CjieqiUserHonor_un%3D%26%23x65B0%3B%26%23x624B%3B%26%23x4E0A%3B%26%23x8DEF%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1552979371; path=/, jieqiVisitInfo=jieqiUserLogin%3D1552979371%2CjieqiUserId%3D380601; expires=Thu, 19-May-2022 16:56:10 GMT; path=/
分析可得:
第一处的PHPSESSID=jrh3e8u399kgdm5mh63bpibms1v6i6pc;为进入登陆也时得到的临时cookie,这个没cookie没有记录登陆状态
第二处的PHPSESSID=7idql1ec5qcfo5mijnv717jgmhreidrn;为记录登录状态的新cookie,使用这个发送请求即可
最后一步,使用正则获取第二个PHPSESSID里的cookie并且加入到请求头中,即可完成登陆
'''
w8LoginHeader.update({'cookie':'PHPSESSID='+re.findall('PHPSESSID=(.*?); expires',w8Respone.headers['Set-Cookie'])[1],})

# 登陆后主页
w8IndexResone = requests.get(url=w8IndexUrl,headers=w8LoginHeader)
w8IndexResone.encoding = chardet.detect(w8IndexResone.content)['encoding']
if w8IndexResone.encoding == "GB2312":
    w8IndexResone.encoding = "GBK"
if '退出登录' in w8IndexResone.text:
    print('登陆成功！')
else:
    print('登陆失败！')
print(w8IndexResone.cookies.items())

# 退出
w8ResponeOut = requests.get(url=w8LoginOutUrl,headers=w8LoginHeader)
w8ResponeOut.encoding = chardet.detect(w8ResponeOut.content)['encoding']
if w8ResponeOut.encoding == "GB2312":
    w8ResponeOut.encoding = "GBK"
if '您已经成功退出' in w8ResponeOut.text:
    print('您已经成功退出！')
else:
    print('退出失败！')
print(w8ResponeOut.cookies.items())