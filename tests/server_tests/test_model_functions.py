import unittest

from server import app
from server.article.model import NewsItem

class TestModelFunctions(unittest.TestCase):
	
	def setUp(self):
		self.news_item = NewsItem(mongo_db='test')
		self.news_item.insert({
			"link": "http://www.bbc.com/news/world-40327934",
			"title": "Syria conflict: Why are air combat kills so rare?",
			"content": "Serious Confilct"
		})

		self.news_item.insert({
			"link": "http://www.bbc.com/news/world-40327935",
			"title": "Obama",
			"content": "mother ship"
		})

		self.news_item.insert({
			"link": "http://www.bbc.com/news/world-40327939",
			"title": "hakunama ta ta",
			"content": "obama"
		})

	def tearDown(self):
		self.news_item.clear()

	def test_get_all(self):
		assert self.news_item.get_all(100, 100).count() == 3

	def test_search(self):
		assert self.news_item.search("syria", 100, 100).count() == 1
		assert self.news_item.search("obama", 100, 100).count() == 2



