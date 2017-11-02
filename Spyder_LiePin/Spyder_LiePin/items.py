# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpyderLiepinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    companyName = scrapy.Field()
    salary = scrapy.Field()
    address = scrapy.Field()
    pushDate = scrapy.Field()
    url = scrapy.Field()
    jobinfo = scrapy.Field()
    companyInfo = scrapy.Field()

