import requests
import datetime
import re
from urllib.parse import unquote,urlparse

# 需要爬取的网站列表&&用于Tracker地址提取的正则
urlList_url_RE = {
'https://share.dmhy.org/':['title="磁力下載"href="([\s\S]*?)">([\s\S]*?)</a>',True],
'https://share.dmhy.org/topics/list/page/2':['title="磁力下載"href="([\s\S]*?)">([\s\S]*?)</a>',True],
'https://share.dmhy.org/topics/list/page/3':['title="磁力下載"href="([\s\S]*?)">([\s\S]*?)</a>',True],
'https://share.dmhy.org/topics/list/page/4':['title="磁力下載"href="([\s\S]*?)">([\s\S]*?)</a>',True],
'https://share.dmhy.org/topics/list/page/5':['title="磁力下載"href="([\s\S]*?)">([\s\S]*?)</a>',True],
'https://nyaa.pantsu.cat/':['<a href="magnet:?([\s\S]*?)" title="Magnet Link">',False],
'https://nyaa.pantsu.cat/search/2':['<a href="magnet:?([\s\S]*?)" title="Magnet Link">',False],
'https://nyaa.pantsu.cat/search/3':['<a href="magnet:?([\s\S]*?)" title="Magnet Link">',False],
'https://nyaa.pantsu.cat/search/4':['<a href="magnet:?([\s\S]*?)" title="Magnet Link">',False],
'https://nyaa.pantsu.cat/search/5':['<a href="magnet:?([\s\S]*?)" title="Magnet Link">',False],
'https://mikanani.me/Home/Classic':[' <a data-clipboard-text="([\s\S]*?)"',False],
'https://mikanani.me/Home/Classic/2':[' <a data-clipboard-text="([\s\S]*?)"',False],
'https://mikanani.me/Home/Classic/3':[' <a data-clipboard-text="([\s\S]*?)"',False],
'https://mikanani.me/Home/Classic/4':[' <a data-clipboard-text="([\s\S]*?)"',False],
'https://mikanani.me/Home/Classic/5':[' <a data-clipboard-text="([\s\S]*?)"',False],
# 'https://acg.rip/':[' <a data-clipboard-text="([\s\S]*?)"',False],
# 'http://bt.acg.gg/':[' <a data-clipboard-text="([\s\S]*?)"',False],
# 'http://www.kisssub.org/':[' <a data-clipboard-text="([\s\S]*?)"',False],

}

trackerListFileNames = {
    'animeTrackers_best':[''],
    'animeTrackers_all':[],
    'animeTrackers_bad':[],
    'animeTrackers_all_udp':[],
    'animeTrackers_all_http':[],
    'animeTrackers_all_https':[],
    'animeTrackers_all_ws':[],
    'animeTrackers_best_ip':[],
    'animeTrackers_all_ip':[],
}

P = {
    "http":"http://127.0.0.1:1080",
    "https":"https://127.0.0.1:1080",
}

# 网页下载器
class Spider(object):
    def __init__(self, url):
        self.url = url
        self._header = {
            'Referer': 'https://www.google.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        }
        self.url_RE = urlList_url_RE[url][0]
        self.nbsp_del = urlList_url_RE[url][1]

    def htmlDownloader(self):
        '''
        HTML下载函数
        :return:目标网页响应内容
        '''
        self.html = requests.get(url=self.url, headers=self._header)
        # self.html = requests.get(url=self.url, headers=self._header, proxies=P)
        self.html.encoding='utf-8'
        return self.html.text

    def re_DMHY(self,html_text, re_pattern, nbsp_del=True):
        '''
        增则过滤函数
        :param html_text: 字符串，网页的文本
        :param re_pattern: 字符串，正则表达式
        :param nbsp_del: 布尔值，控制是否以去除换行符的形式抓取有用信息
        :return:
        '''
        self.pattern = re.compile(re_pattern)
        if nbsp_del:
            return self.pattern.findall("".join(html_text.split()))
        else:
            return self.pattern.findall(html_text)

    def cutMagnet(self,cutMagnet):
        '''
        裁剪磁链头部，并且进行简单tracker去重
        :return: 保留tracker的部分
        '''

        self.trackList = []
        for i in cutMagnet:
            # 合并列表,并进行url解码（例如：http%3A%2F%2F104.238.198.186%3A8000%2Fannounce，解码成：http://104.238.198.186:8000/announce）
            if "tuple" in str(type(i)):
                self.trackList += list(map(lambda x:unquote(x), i[0].replace("&amp;", "&").split('&tr=')[1:]))
            else:
                self.trackList += list(map(lambda x:unquote(x), i.replace("&amp;", "&").split('&tr=')[1:]))
        # 同站去重
        self.trackList = list(set(self.trackList))
        print('同站去重,得到 %s 条Tracker地址'%len(self.trackList))
        return self.trackList

    def main_Spider(self):
        '''
        爬虫主函数
        :return:初步处理的Trackerl列表
        '''
        self.magnetList = list(self.re_DMHY(self.htmlDownloader(), self.url_RE, self.nbsp_del))
        print('从 %s 匹配到磁性链接 %s 条'%(self.url,len(self.magnetList)))
        return self.cutMagnet(self.magnetList)

def socket_is_opened(url,timout):
    '''
    磁性链接测试函数
    :param url: 字符串，需要测试的tracker服务器地址
    :param timout: int类型，测试tracker服务器地址的超时时间
    :return: 布尔值
    '''
    result = urlparse(url)
    import socket
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(timout)
    try:
        if result.port is None:
            if result.scheme is 'http':
                sk.connect(result.hostname, 80)
            if result.scheme is 'https':
                sk.connect(result.hostname, 443)
        else:
            sk.connect((result.hostname, result.port))
        print(url + ' is alive!')
        return True
    except socket.error:
        print(url + ' is not alive!')
        return False
    finally:
        sk.close()

def readmeEditor(fileName='README.md'):
    '''
    说明书更新函数，按时间更新说明书的某些内容
    :param fileName: 字符串，说明书的文件名，可带绝对路径
    :return: 无返回值
    '''

    try:
        # 读取说明书，并保存为列表
        with open(fileName, 'r', encoding="utf-8") as f:
            lines = f.readlines()

        # 自动查找包含‘Updated’在文本哪一行，如果未查找到默认值0，并修改改行文本内容
        lines[lines.index(list(filter(lambda x: x if 'Updated' in x else 0, lines))[0])] = '#### 更新时间（Updated）: %s \n' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 自动查找包含关键字在文本哪一行，如果未查找到默认值0，并修改改行文本内容
        for i in trackerListFileNames:
            lines[lines.index(list(filter(lambda x: x if i in x else 0, lines))[0])] = '* {name}({num} 个tracker) => https://github.com/DeSireFire/animeTrackerList/blob/master/{filename}.txt \n'.format(name = i, num = len(trackerListFileNames[i]), filename = i)

        # 重写说明书
        with open(fileName, 'w', encoding="utf-8") as file_write:
            for i in lines:
                file_write.write(i)
    except IOError as e:
        print('读写说明书出错！%s'%e)

def trackerList(trackerList,fileName):
    '''
    tracker列表文本生成器
    :param trackerList:跟踪器列表
    :param fileName: 创建的文本名字
    :return: 无返回值
    '''
    if trackerList:
        try:
            # 生成文本文件
            with open(fileName+'.txt', 'w', encoding="utf-8") as file_write:
                for i in trackerList:
                    file_write.write(i+'\n')
        except IOError as e:
            print('创建文本出错！%s'%e)
    else:
        print('列表为空，跳过写入')

def trackerListHandler(trackerListResult):
    '''
    跟踪器列表分装整理函数
    :param trackerListResult: 爬虫获取到的简单去重的列表
    :return: 无返回值，直接调用trackerList函数
    '''
    # 先排除坏tracker,再从好的trackers选出快速的trackers
    for i in trackerListResult:
        print('[%s/%s]'%(trackerListResult.index(i)+1,len(trackerListResult)+1))
        if socket_is_opened(i,10):
            trackerListFileNames['animeTrackers_all'].append(i)
            if socket_is_opened(i,1):
                trackerListFileNames['animeTrackers_best'].append(i)
        else:
            trackerListFileNames['animeTrackers_bad'].append(i)

    # 从快速trackers选出带IP的trackers地址
    for i in trackerListFileNames['animeTrackers_best']:
        if checkip(i):
            trackerListFileNames['animeTrackers_best_ip'].append(i)
    # 从好的trackers选出带IP的trackers地址
    for i in trackerListFileNames['animeTrackers_all']:
        if checkip(i):
            trackerListFileNames['animeTrackers_all_ip'].append(i)
    # 从好的trackers分类trackers地址
    for i in trackerListFileNames['animeTrackers_all']:
        if 'udp:' in i:
            trackerListFileNames['animeTrackers_all_udp'].append(i)
        elif 'http:' in i:
            trackerListFileNames['animeTrackers_all_http'].append(i)
        elif 'https:' in i:
            trackerListFileNames['animeTrackers_all_https'].append(i)
        elif 'wss:' in i:
            trackerListFileNames['animeTrackers_all_ws'].append(i)



def checkip(ip):
    '''
    判断是否为IP地址函数
    :param ip: 字符串，ip地址
    :return:
    '''
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    # print(ip.split('/'))
    # ['https:', '', '104.31.112.235:443', 'announce']
    for i in ip.split('/'):
        if p.match(i):
            return True
    return False

def autoGithub(choose):
    '''
    自动上传github的工具
    :param choose: 布尔值，为True为上传到github,反之为从github拉取同步
    :return:
    '''
    # import subprocess
    import os
    # res = subprocess.Popen('bash autopush.sh', shell=True)
    if choose:
        print('上传到repo')
        tempPid = os.popen('bash autopush.sh')
        resPid = tempPid.readlines()
        tempPid.close()
        for i in resPid:
            print(i)
        if 'Already up-to-date.' in resPid:
            return True
        else:
            return False

    else:
        print('从repo同步')
        tempPid = os.popen('git pull')
        resPid = tempPid.readlines()
        tempPid.close()
        for i in resPid:
            print(i)

def printTime(inc = 86400):
    '''
    定时任务工具
    Timer 函数第一个参数是时间间隔（单位是秒），第二个参数是要调用的函数名，第三个参数是调用函数的参数(tuple)
    :param inc: 整数型，单位秒，默认值为86400（24小时）
    :return:
    '''
    from threading import Timer,activeCount
    print('于 %s 进入新一轮任务计时'%datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print('当前线程数为{}'.format(activeCount()))
    t = Timer(inc, ATL_main)
    t.start()

def ATL_main():
    print('自动启动,时间：%s'%datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # 同步github
    autoGithub(0)
    temp = []
    for i in urlList_url_RE:
        i_DMHY = Spider(i)
        temp += i_DMHY.main_Spider()
    temp = list(set(temp))
    print('共获取了 %s 条不同的Trackers'%len(temp))
    trackerListHandler(temp)
    for i in trackerListFileNames:
        print('%s:%s'%(i,trackerListFileNames[i]))
        trackerList(trackerListFileNames[i],i)
    # 写入readme
    readmeEditor()
    # 上传github
    autoGithub(1)
    # 循环调用，下一次调用为一天后
    printTime(86400)

if __name__ == '__main__':
    printTime(5)

    # socket_is_opened(temp[1:10],1)
    # socket_is_opened(['wss://tracker.fastcast.nz:443/announce'],1)

    # readmeEditor()
    # i_DMHY = Spider('https://nyaa.pantsu.cat/')
    # i_DMHY = Spider('https://share.dmhy.org/')
    # i_DMHY = Spider('https://mikanani.me/Home/Classic')
    # i_DMHY = Spider('https://acg.rip/')
    # i_DMHY = Spider('http://www.kisssub.org/')
    # print(i_DMHY.htmlDownloader())
    # print(i_DMHY.main_Spider())

    # autoGithub(1)

    # readmeEditor()
