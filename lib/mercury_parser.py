import requests

class MarcuryParser(object):
	endpoint = 'https://mercury.postlight.com/parser'
	api_key = ''

	def __init__(self, api_key):
		self.api_key = api_key
		self.headers = {'x-api-key': api_key}

	def parse(self, url):
		params = {
			'url' : url
		}

		resp = requests.get(self.endpoint, headers=self.headers, params=params)
		if resp.text:
			return resp.json()
		return {}
