from Spyder_LiePin.items import SpyderLiepinItem
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
import re

class Sypder_LPR(RedisSpider):
    name = 'liepin'
    c = 'liepin:start_urls'
    #redis 要记得提前注册
    #redis-cli lpush liepin:start_urls https://www.liepin.com/zhaopin/?key=python

    def rep_handler(self, var):
        return var.replace('\n', '').replace('\t', '').replace('\r', '')

    def parse(self, response):
        body = self.rep_handler(response.body.decode('utf8'))
        info = re.findall(
            'class="job-info">(.*?)href="(.*?)"(.*?)_9\'\)">(.*?)</a>(.*?)warning">(.*?)</span>(.*?)"area">(.*?)</a>(.*?)edu">(.*?)</span>(.*?)</span>(.*?)title="(.*?)"',
            body)

        for item in info:
            items = SpyderLiepinItem()
            items["jobName"] = item[3]
            items["salary"] = item[5]
            items["address"] = item[7]
            items["pushDate"] = item[12]
            items["url"] = item[1]

            yield Request(url=items["url"], callback=self.detail, meta={"item": items})

    def detail(self, response):
        items = response.meta["item"]
        body = self.rep_handler(response.body.decode('utf8'))
        jobinfo = re.findall('class="content content-word">(.*?)</div>', body)
        if len(jobinfo) > 0:
            items["jobinfo"] = jobinfo[0]
        companyInfo = re.findall('class="info-word">(.*?)</div>', body)
        if len(companyInfo) > 0:
            items["companyInfo"] = companyInfo[0]
        companyName = re.findall('<h1(.*?)<h3>(.*?)title="(.*?)"', body)
        if len(companyName) > 0:
            items["companyName"] = companyName[0][2]
        yield items