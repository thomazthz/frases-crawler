import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


#class FrasesPipeline(object):
#    def process_item(self, item, spider):
#        return item
    
        
class MongoPipeline(object):

#	collection_name = ""

	def __init__(self, mongo_uri, mongo_db, collection_name):
		self.mongo_uri = mongo_uri
		self.mongo_db = mongo_db
		self.collection_name = collection_name

	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			mongo_uri = crawler.settings.get('MONGODB_URI'),
			mongo_db = crawler.settings.get('MONGODB_DB', 'items'),
			collection_name = crawler.settings.get('MONGODB_COLLECTION'),
		)

	def open_spider(self, spider):
		self.client = pymongo.MongoClient(self.mongo_uri)
		self.db = self.client[self.mongo_db]

	def close_spider(self, spider):
		self.client.close()

	def process_item(self, item, spider):
		self.db[self.collection_name].insert(dict(item))
		return item

    