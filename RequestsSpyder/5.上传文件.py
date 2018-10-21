"""
requests 爬虫
来而不往非礼也，既然有了下载保存，那么肯定也有上传
这里不再使用get方法，而是使用post方法！
以上传图片到图床https://sm.ms 为例
这是图床的API说明文档：https://sm.ms/doc/

了解一下：post()
requests.post(url,data=data,header=header,files=files)
- data设置body数据
- header设置请求头
- files设置上传的文件
"""
import requests,re
myheader = {
'Host':'sm.ms',
}
files = {'smfile':open('1.jpg','rb')}
req = requests.post(url="https://sm.ms/api/upload",files=files)
print(req.json())
'''
成功以后运行结果如下：
{'code': 'success', 'data': {'width': 150, 'height': 155, 'filename': '1.jpg', 'storename': '5bc9d5e084d19.jpg', 'size': 28902, 'path': '/2018/10/19/5bc9d5e084d19.jpg', 'hash': 'nVgKA5E8tLcofJx', 'timestamp': 1539954144, 'ip': '171.36.8.151', 'url': 'https://i.loli.net/2018/10/19/5bc9d5e084d19.jpg', 'delete': 'https://sm.ms/delete/nVgKA5E8tLcofJx'}}
其他结果均为失败！
由于只是测试所以就不要给别人的图床增加那么多负担啦,这是浪费资源，何况这是一个免费的良心图床，
不要让贡献者寒心，所以测试完，记得删除！这是礼仪！
'''
req = requests.post(url=req.json()['data']['delete'])
pattern = re.compile('<div class="bs-callout bs-callout-warning" style="border-left-width: 2px;">([\s\S]*?)</div>',re.S)
titles = re.findall(pattern,req.text)
print(titles)
