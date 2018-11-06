import requests,chardet,re
from spyder.HtmlDownloader import Html_Downloader
import config

P = {
    "http":"http://114.113.126.86:80",
    "https":"https://101.37.79.125:3128",
    # "https":"https://106.60.44.145:80",

}

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


if __name__ == '__main__':
    try:
        # 网页请求成功
        r = requests.get(url='https://www.wenku8.net/book/1.htm', headers=config.get_header(), timeout=10 ,proxies=P)

        # 获取网页编码格式，并修改为request.text的解码类型
        r.encoding = chardet.detect(r.content)['encoding']

        # 网页请求OK或者请求得到的内容过少，判断为连接失败
        if (not r.ok) or len(r.content) < 500:
            raise ConnectionError
        else:
            # reglux_list(parser['pattern']["novel_info"],r.text)
            print(r.text)
    except Exception as e:
        print(e)
    # for url in config.parserList[0]["urls"]:
    #     response = Html_Downloader.download(url)
    #     if response is not None:
    #         reglux_list(config.parserList[0]['pattern']["novel_info"], response)
    #     else:
    #         print("%s 爬取失败" % url)