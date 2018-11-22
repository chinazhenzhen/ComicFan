# -*- coding: utf-8 -*-

#pipeline作用
#清理html数据
#验证爬取数据，检查爬取字段
#查重并丢弃重复内容
#将爬取结果保存到数据库

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy import log

class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        # 类方法，依赖注入方式。通过crawler拿到全局配置的配置信息。
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        # open_spider 当spider开启时，这个方法被调用，主要进行了一些初始化操作/
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        #process_item 方法执行了数据库插入操作。
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):
        # close_spider 当spider关闭时，这个方法会被调用。将数据库连接关闭。
        self.client.close()


class SpiderModulePipeline(object):
    def process_item(self, item, spider):
        return item
