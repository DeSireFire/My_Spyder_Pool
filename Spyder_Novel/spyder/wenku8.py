import requests,chardet,re
import random
import json
import config
import spyder.HtmlHandler
import spyder.HtmlDownloader

if __name__ == '__main__':
    # try:
        # # 网页请求成功
        # r = requests.get(url='https://www.wenku8.net/novel/2/2475/index.htm', headers=config.get_header(), timeout=10)
        #
        # # 获取网页编码格式，并修改为request.text的解码类型
        # r.encoding = chardet.detect(r.content)['encoding']
        #
        # # 网页请求OK或者请求得到的内容过少，判断为连接失败
        # if (not r.ok) or len(r.content) < 500:
        #     raise ConnectionError
        # else:

    # except Exception as e:
    #     print(e)
    # for url in config.parserList[0]["urls"]:
    #     response = Html_Downloader.download(url)
    #     if response is not None:
    #         reglux_list(config.parserList[0]['pattern']["novel_info"], response)
    #     else:
    #         print("%s 爬取失败" % url)
    r = spyder.HtmlDownloader.Html_Downloader.download(url='https://www.wenku8.net/novel/2/2475/index.htm')

    # pattern = re.compile(config.parserList[0]["pattern"]["Chapter"]['novel_title'])
    # matchs = pattern.findall(r)
    matchs = spyder.HtmlHandler.reglux_list({'novel_title':r'<td class="vcss" colspan="4">(.*?)</td>',},r)
    print(matchs)