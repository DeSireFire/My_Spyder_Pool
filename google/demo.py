import requests,re

myheaders1 = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    # "Referer":"https://lnovel.cc/",
}
proxies = {
  'http': 'http://192.168.0.107:10808',
  'https': 'http://192.168.0.107:10808',
}
# req = requests.get("https://www.google.com/search?q=django&&tbs=qdr:w",headers=myheaders1,proxies=proxies)
req = requests.get("https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=intitle:powered+by+dedecms&rsz=8&start=57",headers=myheaders1)
print(req.text)
# pattern = re.compile('data-za-element-name="Title">(.*?)</a>',re.S)
# titles = re.findall(pattern,req.text)
# print(titles)