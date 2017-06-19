from pymongo import MongoClient, IndexModel

from config import MONGO_URI, MONGO_DB

class NewsItem(object):
	mongo_con = None
	db = None

	def __init__(self, mongo_uri=MONGO_URI, mongo_db=MONGO_DB):
		self.mongo_con = MongoClient(mongo_uri)
		self.db = self.mongo_con[mongo_db]
		self.create_indexes()
	
	def __del__(self):
		self.mongo_con.close()
	
	def create_indexes(self):
		# Create Index for Full Text Search
		self.db.news_items.create_index([('$**', 'text')])

		# Create Index for not having duplicate article
		self.db.news_items.create_index("link", unique=True)

	def get_all(self, page, limit):
		return self.db.news_items.find({}).skip(limit*(page-1)).limit(limit)

	def search(self, query, page, limit):
		return self.db.news_items.find({"$text": {"$search": query}}).skip(limit*(page-1)).limit(limit)

	def insert(self, item): # insert a document
		self.db.news_items.update({'link': item['link'] }, {'$set': dict(item) }, upsert=True) # if no document exists with the link, then insert
		return

	def clear(self): #clears the collection
		self.db.news_items.remove({})
		return