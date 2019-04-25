import requests,re
myheader = {
'Host':'sm.ms',
}

proxies = { "http": "http://203.150.142.138:8080", "https": "http://203.150.142.138:8080", }
req = requests.get(url="http://192.168.0.102:5360/tools/imgUrlSave/?imgUrl=https://img2.gelbooru.com//images/8b/48/8b481fa761a11cd66a41f6c9268d5284.jpg",headers= myheader)
print(type(req.json()))
'''
成功以后运行结果如下：
{'code': 'success', 'data': {'width': 150, 'height': 155, 'filename': '1.jpg', 'storename': '5bc9d5e084d19.jpg', 'size': 28902, 'path': '/2018/10/19/5bc9d5e084d19.jpg', 'hash': 'nVgKA5E8tLcofJx', 'timestamp': 1539954144, 'ip': '171.36.8.151', 'url': 'https://i.loli.net/2018/10/19/5bc9d5e084d19.jpg', 'delete': 'https://sm.ms/delete/nVgKA5E8tLcofJx'}}
其他结果均为失败！
由于只是测试所以就不要给别人的图床增加那么多负担啦,这是浪费资源，何况这是一个免费的良心图床，
不要让贡献者寒心，所以测试完，记得删除！这是礼仪！
'''
# req = requests.post(url=req.json()['data']['delete'])
# pattern = re.compile('<div class="bs-callout bs-callout-warning" style="border-left-width: 2px;">([\s\S]*?)</div>',re.S)
# titles = re.findall(pattern,req.text)
# print(titles)
