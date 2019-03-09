import requests,re,time,json
URL = 'http://tool.chacuo.net/commontorrentinfo'

FormData = {
# 'data':'https://nyaa.si/download/1123982.torrent',
'data':'http://bt.acg.gg/down.php?date=1542855794&hash=035765ed8d2f15ba7e8fc5274b6afe0c59c260f8',
'type':'torrentinfo',
'arg':'',
'beforeSend':'undefined',
}

_header = {
    'Host':'tool.chacuo.net',
    'Origin':'http://tool.chacuo.net',
    'Referer':'http://tool.chacuo.net/commontorrentinfo',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
def time_decorator(func,**kwargs):
    def run_time(*args,**kwargs):
        start=time.time()
        # print 'start:', start
        func(*args,**kwargs)
        # return res
        stop=time.time()
        print('run_time:%s'%(stop-start))
    return run_time

def Handler(tempStr):
    '''
    处理得到信息，按<tr>标签切除，并替换</th>为：号，最后去除所有html标签
    :param tempStr:符合字典格式的字符串
    :return:
    '''
    data = []
    for n in json.loads(tempStr)['data'][0].split('<tr>'):
        data.append(re.sub(r'</?\w+[^>]*>','',n.replace('</th>',':')))
        print(re.sub(r'</?\w+[^>]*>','',n.replace('</th>',':')))

@time_decorator
def BTtoMagnet(URL,FormData,_header):
    _respone = requests.post(url=URL,data=FormData,headers=_header)
    _respone.encoding = 'unicode_escape'
    Handler(_respone.text)



if __name__ == '__main__':
    BTtoMagnet(URL,FormData,_header)