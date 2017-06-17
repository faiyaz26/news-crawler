# -*- coding: utf-8 -*-

'''
BBC News Article Item
'''


import scrapy
from scrapy.item import Field

class BBCArticle(scrapy.Item):
    title = Field()
    link = Field()
    content = Field()
    author = Field()
    published_at = Field()
