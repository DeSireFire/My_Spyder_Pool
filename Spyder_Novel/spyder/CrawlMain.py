import config
import spyder.HtmlHandler
from spyder.HtmlDownloader import Html_Downloader

print(config.parserList[0]["urls"][0])
c = spyder.HtmlDownloader
req = c.Html_Downloader.download(config.parserList[0]["urls"][0])
if req:
    if spyder.HtmlHandler.endDetection(req):
        info = spyder.HtmlHandler.reglux_list(config.parserList[0]["pattern"]["novel_info"],req)
        print(info)
        if spyder.HtmlHandler.responseAgain(info):
            # 需要二次请求
            req = c.Html_Downloader.download(info["responseAgain"][0])
            print(req)
            if req:
                print(config.parserList[0]["pattern"]["Chapter"])
                Chapter = spyder.HtmlHandler.reglux_list(config.parserList[0]["pattern"]["Chapter"],req)
                print(Chapter)

        else:
            # 不需要二次请求，于当前页完成内容爬取
            print("不需要二次请求，于当前页完成内容爬取")

    else:
        print("到达尽头！")
else:
    print(req)
    print("请求失败，建议continue")