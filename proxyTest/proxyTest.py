# 测试代理IP是否可用
import requests,json

# for debug to disable insecureWarning
requests.packages.urllib3.disable_warnings()

proxyUrl1 = 'http://192.168.37.128:5010/get_all/'
proxyUrl2 = 'http://192.168.37.128:5010/get_all/'
# testUrl = 'https://www.wenku8.net/book/1.htm'
testUrl = 'https://www.bilibili.com/'
# testUrl = 'https://twitter.com/'
# testUrl = 'https://share.dmhy.org'
# testUrl = 'http://www.baidu.com'
# testUrl = 'http://httpbin.org/get'
delProxyUrl = 'http://192.168.37.128:5010/delete?proxy=%s'
# 获取 代理列表s
res = requests.get(url=proxyUrl1)
proxyList = json.loads(res.text)
print(res.text)
for temp in proxyList:
    proxies = {
        'http': 'http://%s'%(temp),
        'https': 'http://%s'%(temp),
    }
    try:
        response = requests.get(testUrl, proxies=proxies, timeout = 15,verify=False)
        if response.status_code == 200:
            print(proxies)
    except Exception as e:
        print(e)
        print('执行删除操作！%s' % temp)
        temps = delProxyUrl % (temp)
        delproxy = requests.get(temps)
        if delproxy.text:
            print('删除成功！')