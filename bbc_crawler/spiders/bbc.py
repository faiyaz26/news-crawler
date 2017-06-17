# -*- coding: utf-8 -*-

'''
Spider for BBC News Site
'''
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import scrapy

from bbc_crawler.items import BBCArticle
from lib.mercury_parser import MarcuryParser
from bbc_crawler.settings import MERCURY_API_KEY

class BBCSpider(scrapy.Spider):
	name = "bbc_crawler"
	start_urls = ['http://www.bbc.com/news']
	allowed_domains  = ["bbc.com"]

	allowed_url_regex = [r'(.)*\/news\/[a-z-]+-\d+']

	mercury_parser = MarcuryParser(MERCURY_API_KEY)

	def valid_url(self, url): # Simple validator to make sure we are fetching only news content
		for url_regex in self.allowed_url_regex:
			if re.match(url_regex, url):
				return True
		return False

	def parse(self, response):
		soup = BeautifulSoup(response.body, 'lxml')

		# all the article item has an anchor tag with class 'nw-o-link-split__anchor'
		for article_anchor in soup.find_all("a", class_="nw-o-link-split__anchor"):
			relative_url = article_anchor.get('href')
			absolute_url = urljoin(response.url, relative_url)
			if self.valid_url(absolute_url):
				yield scrapy.Request(absolute_url, callback=self.parse_article)

	def parse_article(self, response):
		return self.process_article(response.body, response.url)

	def process_article(self, body, url):
		soup = BeautifulSoup(body, 'lxml')
		article_title = soup.find('h1', class_='story-body__h1')
		if article_title: # Parsing a valid/intended article
			article = BBCArticle()
			article['link'] = url
			article['title'] = article_title.string.strip()
			article['content'] = self.mercury_parser.parse(url).get('content', '')
			article['author'] = ''
			article['published_at'] = int(soup.find('div', class_='date--v2').attrs.get('data-seconds'))
			yield article
