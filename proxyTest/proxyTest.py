# 测试代理IP是否可用
import requests,json

proxyUrl1 = 'http://193.112.52.146:8000/?types=0&count=100&country=国内'
proxyUrl2 = 'http://193.112.52.146:8000/?types=0&count=100&country=国外'
# proxyUrl = 'http://www.zzuliacgn.com:8000/?types=0&count=10&country=%E5%9B%BD%E5%A4%96'
testUrl = 'https://www.baidu.com/'
delProxyUrl = 'http://193.112.52.146:8000/delete?ip=%s&port=%s'
# 获取 代理列表
res = requests.get(url=proxyUrl1)
proxyList = json.loads(res.text)
res = requests.get(url=proxyUrl2)
proxyList += json.loads(res.text)
for temp in proxyList:
    proxies = {
        'http': 'http://%s:%s'%(temp[0],temp[1]),
        'https': 'http://%s:%s'%(temp[0],temp[1]),
    }
    try:
        response = requests.get(testUrl, proxies=proxies, timeout = 10,verify=False)
        if requests.status_codes ==200:
            print(print(proxies))
    except Exception as e:
        print(e)
        # if '强迫关闭' in str(e) or '积极拒绝' in str(e):
        #     print('执行删除操作！%s'%temp[0])
        #     temp = delProxyUrl%(temp[0],temp[1])
        #     delproxy = requests.get(temp)
        #     if int(delproxy.text):
        #         print('删除成功！')
        print('执行删除操作！%s' % temp[0])
        temp = delProxyUrl % (temp[0], temp[1])
        delproxy = requests.get(temp)
        if int(delproxy.text):
            print('删除成功！')