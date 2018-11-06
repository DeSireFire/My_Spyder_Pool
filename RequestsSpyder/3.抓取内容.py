"""
requests 爬虫
实现简单的内容抓取
这里以get()方法为例，post等其他方法抓取内容时也可以参考
"""
import requests
import re
# 添加请求头
myheaders1 = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Referer":"https://lnovel.cc/",
}
# req = requests.get("https://www.zhihu.com/explore",headers=myheaders1)
# pattern = re.compile('data-za-element-name="Title">(.*?)</a>',re.S)
# titles = re.findall(pattern,req.text)
# print(titles)
# print('*'*50)
'''
是不是相当的简单呀？
'''
myheaders2 = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Referer":"https://lnovel.cc/",
}
# req = requests.get("https://lnovel.cc/",headers=myheaders2)
# print(req.text)
# print(req.content)
'''
可以观察到，text都是乱码,content是以b开头的内容，但是好一些，起码能看出来是编码了
text： 返回的是Unicode编码的数据
content：返回的是bytes类型的数据

由于这个网站它本身UTF-8编码的，当你再用Unicode编码时会肯定出现乱码了
怎么解决呢？万码之祖当然是bytes了，只要把它解码成utf-8就行，text在这里就不用它了
'''
# print(req.content.decode(encoding="utf-8"))
'''
然后抓取需要的内容！
'''
req = requests.get("https://lnovel.cc/",headers=myheaders2)
pattern = re.compile('<h2 class="mdl-card__title-text">(.*?)</h2>',re.S)
titles = re.findall(pattern,req.content.decode(encoding="utf-8"))
print(titles)
for i in titles:
    print(i)
