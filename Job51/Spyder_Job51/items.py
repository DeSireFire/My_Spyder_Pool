# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Spyder_Job51Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    JobName = scrapy.Field()
    #工作名
    companyName = scrapy.Field()
    #公司名
    salary = scrapy.Field()
    #薪水
    address = scrapy.Field()
    #公司地址
    pushDate = scrapy.Field()
    #发布时间
    url = scrapy.Field()
    #公司url
    jobinfo = scrapy.Field()
    #工作详情
    companyInfo = scrapy.Field()
    #公司详情


