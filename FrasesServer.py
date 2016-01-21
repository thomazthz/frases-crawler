#!/usr/bin/env python
from pymongo import MongoClient
import optparse
import json

class DBServer:

	def __init__(self):
		#import ipdb; ipdb.set_trace()
		self.client = MongoClient()
		self.db = self.client['frasesdb']
		self.collection = self.db['frases']

	def get_phrase_by_author(self, author):
		return self.collection.find_one({'autor': author})



parser = optparse.OptionParser()
parser.add_option('-a', '--author', dest='author', help='Author')

(options, args) = parser.parse_args()

if options.author is None:
	options.author = ''

server = DBServer()
instance = server.get_phrase_by_author(options.author)
#import ipdb; ipdb.set_trace()
author = instance['autor'][0]
phrase = instance['frase'][0]

print (u'%s "%s"' % (phrase, author)).encode('utf-8')
