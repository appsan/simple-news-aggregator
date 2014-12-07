import json
import requests
from flask import abort, Response
from flask.ext.restful import Resource
from bs4 import BeautifulSoup

class Reddit(Resource):

	def get(self):
		try:
			headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3' }
			url = 'http://www.reddit.com/r/all/hot.json?limit=20'
			r = requests.get(url, headers=headers)
			top = json.loads(r.text)

			resp = []
			for entry in top['data']['children']:
				elem = {'title': entry['data']['title'], 'url': entry['data']['url']}
				resp.append(elem)

			return Response(json.dumps(resp), status=200, mimetype='application/json')

		except Exception, e:
			abort(404)


class Hackernews(Resource):

	def get(self):
		try:
			headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3' }
			url = 'https://news.ycombinator.com/'
			r = requests.get(url, headers=headers)
			soup = BeautifulSoup(r.content)

			resp = []
			for td in soup.findAll('td', {'class' : 'title'}):
				for entry in td.findAll('a'):
					elem = {'title': entry.get_text(), 'url': entry['href']}
					resp.append(elem)

			return Response(json.dumps(resp[:21]), status=200, mimetype='application/json')

		except Exception, e:
			abort(404)
	

class Bloomberg(Resource):

	def get(self):
		try:
			headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3' }
			url = 'http://www.bloomberg.com/quickview/popular'
			base_url = 'http://www.bloomberg.com'
			r = requests.get(url, headers=headers)
			soup = BeautifulSoup(r.content)

			resp = []
			for entry in soup.find_all('a'):
				elem = {'title': entry.get_text(), 'url': base_url+entry['href']}
				resp.append(elem)

			return Response(json.dumps(resp), status=200, mimetype='application/json')

		except Exception, e:
			abort(404)


