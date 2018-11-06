import re,requests,config,json

__author__ = 'DeSireFire'

# 页面尽头检测
def endDetection(response,keyList = config.keyList):
    """

    :param response: 检测是不是爬取到了网站的尽头
    :param keyList: 判断到尽头的关键字
    :return: 布尔值
    """
    if response:
        for i in keyList:
            if i in response:
                return False
        return True
    else:
        return False

# 二阶请求检测
def responseAgain(infoDict):
    """
    一般结合reglux_list方法使用，检测config.parserList[X]['pattern']['novel_info']['responseAgain']是否为空
    :param infoDict: 传入键值中有“responseAgain”的字典即可
    :return: 布尔值
    """
    if infoDict['responseAgain']:
        if re.match(r'^https?:/{2}\w.+$', infoDict['responseAgain'][0]):
            # 需要二次请求
            return True
        else:
            # 不需要二次请求,或没匹配到二次请求的地址
            return False
    else:
        return False


def reglux_list(mydict,response):
    """
    遍历正则抓取数据
    :param mydict: 字典类型{key:正则表达式，}
    :param response: request.text
    :return: 字典类型
    """
    temp = {}
    for m,n in mydict.items():
        if '' != n:
            pattern = re.compile(n)
            matchs = pattern.findall(response)
            temp.update({m:matchs,})
        else:
            temp.update({m: list(n),})
    return temp

def proxy_list(url = config.PROXYURL,testURL = config.testURL):
    """
    获取并检测代理池返回的IP
    :param url: 获取IP的代理池地址
    :param testURL: 检测网址
    :return: 一个能用的ip组成的proxies字典
    """
    count = 0 # 获取的IP数
    try:
        r = requests.get(url)
        count = len(json.loads(r.text))
        while count != 0:
            r = requests.get(url)
            ip_ports = json.loads(r.text)
            count = len(ip_ports)
            for i in range(0,4):
                ip = ip_ports[i][0]
                port = ip_ports[i][1]
                proxies = {
                    'http': 'http://%s:%s' % (ip, port),
                    'https': 'https://%s:%s' % (ip, port)
                }
                r = requests.get(testURL, proxies=proxies,timeout=config.TIMEOUT)
                if (not r.ok) or len(r.content) < 500:
                    r = requests.get("http://127.0.0.1:8000/delete?ip=%s&port=%s"%(ip,port))
                else:
                    return proxies

    except Exception as e:
        # print(e)
        return None
