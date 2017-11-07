import urllib,urllib.request,json,re

'''
步骤：
1.导入urllib包
2.发送请求的url地址
3.此网站启动反爬措施，需要带入的headers（如果带有反爬虫措施）
4.构造请求Request
5.携带headers发送request请求

'''

'''
判断是否有反爬措施的步骤：
1. 拿到一个网址后，首先直接去请求，如果响应的数据正常，则说明此网站没有反爬机制，无需在做其他操作
2. 如果拿到的响应数据故障或者没有拿到数据，则说明此网站存在机器人操作，针对机器人操作，首先分析请求中的request header，将此拷贝完之后，放入request中请求，全部带的请求可能存在gzip方式的压缩和解压缩，然后考虑考虑refer和user agent

'''

'''
print('基础爬虫')
my_url = 'https://www.taobao.com/'
my_response = urllib.request.urlopen(my_url)
print(my_response.read())
'''

"""
my_url = 'http://www.cnblogs.com/wly923/archive/2013/05/07/3057122.html'
my_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
}

my_request = urllib.request.Request(my_url,headers=my_headers)

my_response = urllib.request.urlopen(my_request)

my_bytes = my_response.read()

my_str = my_bytes.decode('utf8')

print(my_str)

# my_response.close()

"""

'''
总结：

json.dumps : dict转成str

json.loads:str转成dict
'''
url = r'http://temp.163.com/special/00804KVA/cm_guoji.js?callback=data_callback'

req = urllib.request.Request(url=url,data=None)
res = urllib.request.urlopen(req)
# print(type(res))
# print(res.read().decode("gbk"))
# res.read().decode("gbk")
# datajson = json.loads(json.dumps(res.read().decode("gbk")))
datajson = res.read().decode("gbk")
# print(datajson[14:-1])

str_datajson = json.loads(datajson[14:-1])
# print(str_datajson)
# print(type(str_datajson))
titlelist = []
for dictItem in str_datajson:
    # print(dictItem['title'])
    titlelist.append(dictItem['title'])
with open(r'D:\NE.txt', 'w') as f:
    f.writelines('\n'.join(titlelist))
# tlinklist = []
# for tlink in str_datajson:
#     tlinklist.append(tlink['tlink'])
# with open(r'tlinklist.txt', 'w') as f:
#     f.writelines('\n'.join(tlinklist))