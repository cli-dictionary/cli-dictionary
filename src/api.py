from requests import request
from json import loads

class API():
	def __init__(self, url):
		self.url = url
		self.headers = {
			"Accept": "charset=utf-8",
			"Content-Type": "application/json"
    }

	def get_response(self):
		response = request('GET', self.url, headers=self.headers)
		data = loads(response.text)
		return data
