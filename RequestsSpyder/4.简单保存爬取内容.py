"""
requests 爬虫
实现简单的内容抓取以后，把有用的信息保存下来，此法可用于保存图片、视频、音乐、文本等，这里以图片和文本为例
请求方法以get()方法为例，post等其他方法抓取内容时也可以参考
"""
# 下载图片
# import requests
#
# req = requests.get("http://www.zzuliacgn.cf/static/ZA_Show/img/background/QYMX-logo.png")
# with open("QYMX-logo.png","wb") as f:
#     f.write(req.content)
# print("图片下载完成！")

# 保存文本
import requests
import re
myheaders = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Referer":"https://lnovel.cc/",
}
req = requests.get("https://lnovel.cc/",headers=myheaders)
pattern = re.compile('<h2 class="mdl-card__title-text">(.*?)</h2>',re.S)
titles = re.findall(pattern,req.content.decode(encoding="utf-8"))
print(str(titles))
with open("titles.txt","w") as f:
    f.write(str(titles))
print("文本保存完成！")