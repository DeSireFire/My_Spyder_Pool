# -*- coding: utf-8 -*-
from scrapy.conf import settings
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
#
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Spyder_Job51Pipeline(object):
    '''
    数据的存储，存储到mongodb
    '''
    def __init__(self):
        host = settings['MONGODBHOST']
        port = settings['MONGODBPORT']
        database = settings['MONGODDATABASE']
        conn = pymongo.MongoClient(host=host, port=port)
        self.db = conn[database]['job51table']


    def process_item(self, item, spider):
        #entrypoint中的调用
        items = dict(item)
        self.db.insert(items)
        #插入
        return item

    # def process_item2(self, item, spider):
    #     #entrypoint中的调用
    #     items = dict(item)
    #     self.db.insert(items)
    #     return item