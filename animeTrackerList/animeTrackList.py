import requests
import time
import re
from urllib.parse import unquote,urlparse

# 需要爬取的网站列表&&用于Tracker地址提取的正则
urlList_url_RE = {
'https://share.dmhy.org/':['title="磁力下載"href="([\s\S]*?)">([\s\S]*?)</a>',True],
'https://share.dmhy.org/topics/list/page/2':['title="磁力下載"href="([\s\S]*?)">([\s\S]*?)</a>',True],
'https://share.dmhy.org/topics/list/page/3':['title="磁力下載"href="([\s\S]*?)">([\s\S]*?)</a>',True],
'https://nyaa.pantsu.cat/':['<a href="magnet:?([\s\S]*?)" title="Magnet Link">',False],
'https://mikanani.me/Home/Classic':[' <a data-clipboard-text="([\s\S]*?)"',False],
# 'https://acg.rip/':[' <a data-clipboard-text="([\s\S]*?)"',False],
# 'http://bt.acg.gg/':[' <a data-clipboard-text="([\s\S]*?)"',False],
# 'http://www.kisssub.org/':[' <a data-clipboard-text="([\s\S]*?)"',False],

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
        self.html = requests.get(url=self.url, headers=self._header, proxies=P)
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
        print(cutMagnet)
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

def socket_is_opened(urlList,timout):
    '''
    磁性链接测试函数
    :param urlList: 列表，需要测试的tracker服务器地址列表
    :param timout: int类型，测试tracker服务器地址的超时时间
    :return: 无返回值
    '''
    for url in urlList:
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
        except socket.error:
            print(url + ' is not alive!')
        sk.close()

def readmeEditor():
    pass

if __name__ == '__main__':
    temp = []
    for i in urlList_url_RE:
        i_DMHY = Spider(i)
        temp += i_DMHY.main_Spider()
    temp = list(set(temp))
    print('共获取了 %s 条不同的Trackers'%len(temp))
    print(temp)
    socket_is_opened(temp[1:10],1)


    # i_DMHY = Spider('https://nyaa.pantsu.cat/')
    # i_DMHY = Spider('https://share.dmhy.org/')
    # i_DMHY = Spider('https://mikanani.me/Home/Classic')
    # i_DMHY = Spider('https://acg.rip/')
    # i_DMHY = Spider('http://www.kisssub.org/')
    # print(i_DMHY.htmlDownloader())
    # print(i_DMHY.main_Spider())