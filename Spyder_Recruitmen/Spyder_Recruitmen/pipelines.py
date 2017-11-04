# -*- coding: utf-8 -*-
from scrapy.conf import settings
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpyderRecruitmenPipeline(object):

    host = settings['MONGODBHOST']
    port = settings['MONGODBPORT']
    database = settings['MONGODDATABASE']
    # RecruitmenWeb = 'RecruitmenWeb_Other'
    conn = pymongo.MongoClient(host=host, port=port)
        # conn = pymongo.MongoClient(host=host, port=port)
        # self.db = conn[database]['%s' % RecruitmenWeb]
        # if len(RecruitmenWeb) != '':
        #     self.db = conn[database]['%s'%RecruitmenWeb]
        #     # self.db = conn[database]['LiePin_Recruitmen_table']
        # else:
        #     self.db = conn[database]['RecruitmenWeb_Other']

    def process_item(self, item, spider):
        table_name = str(spider.name)
        RecruitmenWeb = dict(item)
        self.db = self.conn[self.database]['%s_table' % table_name]
        self.db.insert(RecruitmenWeb)
        print('存储成功！')
        return item