#!/usr/bin/env python

import sys
import json
import tweepy
import os
import time
import re
import requests

from bs4 import BeautifulSoup
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from urllib.request import urlopen

consumer_key = "EPmNtSbK0VEX9JMyTeLr8WLLa"
consumer_secret = "j0bhW7iOnBuR9XcNEpKdLIyWmrAy2YMhzbP3AIZabL3EmtmJmv"
access_token = "1149105082442514434-amuNTlY7ef90gLOpIl1lW0Jfkx5NFz"
access_token_secret = "O8OZ7dkO6zoyCXRu2cnjuEDLZO68HuAn81XHxPUeYlIMS"

dir_name = 'data'
file_path = os.path.abspath(dir_name + '/twitter_data1.txt')
dir_path = os.path.abspath(dir_name)

# If the 'data' folder doesn't exist, create it.
if not os.path.exists(dir_path):
	os.makedirs(dir_path)

file = open(file_path, 'a') # change back to a+ when finished!

file_num = 1
doneCrawling = False

class twitterCrawler(StreamListener):

	def on_data(self, data):
		global file
		global file_num
		global doneCrawling

    	#2GB data reached
		if (file_num >= 200): # 200
			print("2GB of data reached \n")
			doneCrawling = True
			return False

    	#10MB reached. Open new txt file. 
		if (file.tell() >= 10000000): # 1000000
			print("10 MB OF DATA REACHED, STARTING NEW PAGE \n")
			file.close()		   # close file

			file_num += 1
			file_path = dir_name + '/twitter_data' + str(file_num) + '.txt'
			file = open(file_path, 'a') # if next file doesn't exist, create + open it

		print(data)
		file.write(data)
		return True

	def on_error(self, status):
		print(status)
		if (status == 420):
			print("Too many requests for twitter API, please wait 30 seconds.")
			return False

if __name__ == '__main__':

	while doneCrawling != True:
		try:
			#This handles Twitter authetification and the connection to Twitter Streaming API
			l = twitterCrawler()
			auth = OAuthHandler(consumer_key, consumer_secret)
			auth.set_access_token(access_token, access_token_secret)
			stream = Stream(auth, l)

			#Bounded box location. At the moment, it's around the US
			stream.filter(locations=[-128.2, 21.5, -58.9, 48.6])

			parse_data()
		except Exception as e:
			print("Exception: ")
			print(e)
			time.sleep(30)
			print("Resume crawling")
			pass

	file.close()

