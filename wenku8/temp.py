import requests,chardet
url = 'http://t1.aixinxi.net/o_233qwe6667788.txt'
resRespone = requests.get(url=url,)
resRespone.encoding = chardet.detect(resRespone.content)['encoding']
if resRespone.encoding == "GB2312":
    resRespone.encoding = "GBK"
print(resRespone.text)