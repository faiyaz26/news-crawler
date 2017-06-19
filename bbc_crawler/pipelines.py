# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from server.article.model import NewsItem

class MongoPipeline(object):

	def process_item(self, item, spider):
		NewsItem().insert(dict(item))
		return item
