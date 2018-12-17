# -*- coding: utf-8 -*-
import scrapy
# import Scrapy_BT.Scrapy_BT.tools.test
from Scrapy_BT.items import dmhyItem

class DmhySpider(scrapy.Spider):
    name = "dmhy"
    allowed_domains = ["share.dmhy.org"]
    start_urls = ['https://www.dmhy.org/topics/list/page/1']

    def parse(self, response):
        # dmhys = response.css('.title')
        dmhys = response
        print(self.start_urls)
        # print("这里瞩目一下！！！！！response：%s"%dmhys.text)
        print("这里瞩目一下！！！！！response：%s"%type(dmhys))
        # for dmhy in dmhys:
        #     item = dmhyItem()
        #     item['rdName'] = dmhy.css('.title')
        #     item['rdUpTime'] = dmhy.css('.title')
        #     item['rdSize'] = dmhy.css('.title')
        #     item['rdUpNum'] = dmhy.css('.title')
        #     item['rdDownloadNum'] = dmhy.css('.title')
        #     item['rdInfo'] = dmhy.css('.title')
        #     item['rdOK'] = dmhy.css('.title')
        #     item['rdURLS'] = dmhy.css('.title')
        #     item['rdType'] = dmhy.css('.title')
        #     item['rdView'] = dmhy.css('.title')
        #     yield item

        _next = response.css('a::attr("href")').extract_first()
        print("这里瞩目一下！！！！！%s" % _next)
        url = response.urljoin(_next)
        print("这里瞩目一下！！！！！%s"%url)
        yield scrapy.Request(url=url,callback=self.parse)
