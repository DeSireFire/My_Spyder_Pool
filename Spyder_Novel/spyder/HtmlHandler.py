import re,requests,config,json

__author__ = 'DeSireFire'

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
    print(temp)
    return temp

def proxy_list(url = config.PROXYURL,testURL = 'http://ip.chinaz.com/'):
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
                r = requests.get(testURL, proxies=proxies)
                if (not r.ok) or len(r.content) < 500:
                    r = requests.get("http://127.0.0.1:8000/delete?ip=%s"%ip_ports[i][0])
                else:
                    return proxies

    except Exception as e:
        print(e)
    return None