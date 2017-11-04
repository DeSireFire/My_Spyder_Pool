# -*- coding: utf-8 -*-
from scrapy.conf import settings
import pymongo,re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpyderRecruitmenPipeline(object):

    host = settings['MONGODBHOST']
    port = settings['MONGODBPORT']
    database = settings['MONGODDATABASE']
    conn = pymongo.MongoClient(host=host, port=port)

    def getNoHtmlBody(var):
        body = None
        try:
            dr = re.compile(r'<[^>]+>', re.S)
            body = dr.sub('', var)
        except Exception as ex:
            print(ex)
        return body

    def process_item(self, item, spider):
        table_name = str(spider.name)
        RecruitmenWeb = dict(item)
        self.db = self.conn[self.database]['%s_table' % table_name]
        self.db.insert(RecruitmenWeb)
        print('存储成功！')
        return item