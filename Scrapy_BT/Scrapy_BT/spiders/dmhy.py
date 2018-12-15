# -*- coding: utf-8 -*-
import scrapy
# import Scrapy_BT.Scrapy_BT.tools.test
from Scrapy_BT.items import dmhyItem

class DmhySpider(scrapy.Spider):
    name = "dmhy"
    allowed_domains = ["share.dmhy.org"]
    start_urls = ['http://share.dmhy.org/']

    def parse(self, response):
        # dmhys = response.css('.tag')
        # for dmhy in dmhys:
        #     item = dmhyItem()
        #     item['rdName'] = dmhy.css('.text')
        #     item['rdUpTime'] = dmhy.css('.text')
        #     item['rdSize'] = dmhy.css('.text')
        #     item['rdUpNum'] = dmhy.css('.text')
        #     item['rdDownloadNum'] = dmhy.css('.text')
        #     item['rdInfo'] = dmhy.css('.text')
        #     item['rdOK'] = dmhy.css('.text')
        #     item['rdURLS'] = dmhy.css('.text')
        #     item['rdType'] = dmhy.css('.text')
        #     item['rdView'] = dmhy.css('.text')
        #     yield item
        #
        # _next = response.css('.a::attr("href")').extract_first()
        # url = response.urljoin(_next)
        # yield scrapy.Request(url=url,callback=self.parse)
        pass
