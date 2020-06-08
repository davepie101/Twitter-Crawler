#!/usr/bin/env python
import json
import os
import requests
from bs4 import BeautifulSoup

dir_name = './parsed'
dir_path = os.path.abspath(dir_name)

if not os.path.exists(dir_path):
	os.makedirs(dir_path)

file_num = 3
while file_num <= 200:
	data = []
	file_name = './data/twitter_data' + str(file_num) + '.txt'
	with open(file_name) as f:
		for line in f:
			temp = json.loads(line)

			screen_name = temp['user']['screen_name']
			tweet = temp['text']
			tweet_date = temp['created_at']
			tweet_location = temp['place']
			url = temp['entities']['urls']
			page_title = None
			location = None

			if tweet_location:
				location = tweet_location['full_name']
			if url:
				try:
					expanded_url = temp['entities']['urls'][0]['expanded_url']
					r = requests.get(expanded_url, timeout = 10, verify=False)
					html_content = r.text
					soup = BeautifulSoup(html_content, 'lxml')

					if soup.title:
						page_title = soup.title.string
				
				except requests.exceptions.Timeout:
					print("Timeout occurred")

			jsonItem = {
				"screen_name": screen_name,
				"tweet": tweet,
				"tweet_date": tweet_date,
				"tweet_location": location,
				"page_title": page_title
			}

			data.append(jsonItem)
			print(jsonItem)
	f.close()

	file_name = dir_name + '/parsed_data' + str(file_num) + '.txt'
	file = open(file_name, 'a')
	for line in data:
		print(line)
		json.dump(line, file)
		file.write('\n')
	file.close()

	file_num += 1

