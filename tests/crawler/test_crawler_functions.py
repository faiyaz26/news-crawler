import unittest
from mock import patch

from bbc_crawler.spiders.bbc import BBCSpider

class TestCrawlerFunctions(unittest.TestCase):

	def setUp(self):
		self.spider = BBCSpider()

	def test_valid_url(self):
		self.assertEqual(self.spider.valid_url(url="http://bbc.com/future"),False)
		self.assertEqual(self.spider.valid_url(url="http://bbc.com/news/uk-1334340"),True)

	@patch('bbc_crawler.spiders.bbc.BBCSpider.mercury_parser')
	def test_process_article(self, mercury_parser):
		mercury_parser.parse.return_value = {}
		body = '<h1 class="story-body__h1">Testing</h1><div>abra ca dabra</div>'
		get_item = list(self.spider.process_article(body=body, url="http://bbc.com/news/uk-1334340"))
		assert len(get_item) == 1
		assert get_item[0]['title'] == 'Testing'


		body = '<div>abra ca dabra</div>'
		get_item = list(self.spider.process_article(body=body, url="http://bbc.com/news/uk-1334340"))
		assert len(get_item) == 0