#!/usr/bin/env python
import json
import os
import requests
import lucene
from bs4 import BeautifulSoup
from java.io import File
from datetime import datetime

from org.apache.lucene.document import Document, Field, StringField, TextField
from org.apache.lucene.util import Version
from org.apache.lucene.store import RAMDirectory, FSDirectory
from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import IndexWriter, IndexWriterConfig
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser, QueryParserBase, MultiFieldQueryParser

luceneDirectory = "./index/"


def create_doc(data):
	screen_name = data['user']['screen_name']
	tweet = data['text']
	#tweet_date = data['created_at']
	#tweet_location = data['place']['full_name']
	#url = data['entities']['urls']
	#page_title = ""

	#if url:
		#expanded_url = data['entities']['urls'][0]['expanded_url']
		#r = requests.get(expanded_url)
		#html_content = r.text
		#soup = BeautifulSoup(html_content, 'lxml')

		#if soup.title:
			#page_title = soup.title.string

	doc = Document()
	doc.add(TextField("username", screen_name, Field.Store.YES))
	doc.add(TextField("text", tweet, Field.Store.YES))
	#doc.add(TextField("date", tweet_date, Field.Store.YES))
	#doc.add(TextField("location", tweet_location, Field.Store.YES))
	#doc.add(TextField("url", url, Field.Store.YES))
	#doc.add(TextField("page title", page_title, Field.Store.YES))

	return doc


def index():
	indexFile = File(luceneDirectory).toPath()
	directory = FSDirectory.open(indexFile)

	analyzer = StandardAnalyzer()
	writeConfig = IndexWriterConfig(analyzer)
	writer = IndexWriter(directory, writeConfig)

	file_number = 2
	while file_number <= 200:
		data = []
		file_name = './data/twitter_data' + str(file_number) + '.txt'
		with open(file_name) as f:
			for line in f:
				data.append(json.loads(line))
		f.close()

		for j in data:
			doc = create_doc(j)
			writer.addDocument(doc)

		file_number += 1

if __name__ == '__main__':
	lucene.initVM()
	index()