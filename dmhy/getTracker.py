import requests

URLS = {
    'trackers_best':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt',
    'trackers_all':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt',
    'trackers_all_udp':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_udp.txt',
    'trackers_all_http':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_http.txt',
    'trackers_all_https':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_https.txt',
    'trackers_all_ws':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ws.txt',
    'trackers_best_ip':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt',
    'trackers_all_ip':'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt',
        }

_header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

def getBest(URL,_header):
    '''
    获取git上的Tracker,提高磁链的下载速度
    :param URL: 字符串，请求的URL地址
    :param _header: 字典，请求的网页头部
    :return: 列表，处理好的列表
    '''

    _respone = requests.get(url=URL,headers=_header)
    print(list(map(lambda x: '&tr='+x,_respone.text.split())))
    return list(map(lambda x: '&tr='+x,_respone.text.split()))



if __name__ == '__main__':
    for k in URLS:
        getBest(URLS[k],_header)