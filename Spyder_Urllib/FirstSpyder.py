# coding = utf8

# import urllib.request
# import twisted
# import requests
# from bs4 import BeautifulSoup
# from pprint import pprint



# scrapy.cfg: 项目的配置文件
# tutorial /: 该项目的python模块。之后您将在此加入代码。
# tutorial / items.py: 项目中的item文件.
# tutorial / pipelines.py: 项目中的pipelines文件.
# tutorial / settings.py: 项目的设置文件.
# tutorial / spiders /: 放置spider代码的目录.
'''
myresponse = urllib.request.urlopen('https://www.taobao.com/')
print(myresponse.read())

my_url = 'https://www.taobao.com/'
my_headers = {
    'Host':'www.taobao.com',
    'Referer':'https://www.baidu.com/link?url=jgkQlkDlRq5WKErN8mt-rLlPx5wyxKIo-_64lVM0Gbuu4Lt4LigGYOHj1imD4yzh&wd=&eqid=87e936bb000049160000000359ed5ee4',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',

}
req = urllib.request.Request(my_url,headers=my_headers)
resp = urllib.request.urlopen(req)
page = resp.read()
mystr = page.decode('utf8')
# page.close()

print(page)
'''

# fp = urllib.request.urlopen("https://www.taobao.com/")
#
# mybytes = fp.read()
# # note that Python3 does not read the html code as string
# # but as html code bytearray, convert to string with
# mystr = mybytes.decode("utf8")
#
# fp.close()
#
# print(mystr)