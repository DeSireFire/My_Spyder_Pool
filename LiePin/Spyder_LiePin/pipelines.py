# -*- coding: utf-8 -*-
from scrapy.conf import settings
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpyderLiepinPipeline(object):

    def __init__(self):
        host = settings['MONGODBHOST']
        port = settings['MONGODBPORT']
        database = settings['MONGODDATABASE']
        conn = pymongo.MongoClient(host=host, port=port)
        self.db = conn[database]['LiePintable']

    def process_item(self, item, spider):
        jsondata = dict(item)
        self.db.insert(jsondata)
        print(jsondata)
        return item
