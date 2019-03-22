import requests,chardet
url = 'http://dl.wenku8.com/down.php?type=utf8&id=1'
# url = 'http://t1.aixinxi.net/o_233qwe6667788.txt'
resRespone = requests.get(url=url)
resRespone.encoding = chardet.detect(resRespone.content)['encoding']
if resRespone.encoding == "GB2312":
    resRespone.encoding = "GBK"
print(resRespone.text)