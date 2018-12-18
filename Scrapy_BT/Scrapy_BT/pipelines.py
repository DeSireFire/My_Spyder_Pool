# -*- coding: utf-8 -*-
import codecs,json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyBtPipeline(object):
    def process_item(self, item, spider):
        return item

class dmhyPipeline(object):
    # def __init__(self):
    #     self.file = codecs.open('data_cn.json', 'wb', encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item)) + '\n'
    #     self.file.write(line.decode("unicode_escape"))
    #     return item
    pass