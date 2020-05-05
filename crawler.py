import sys
import json
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key = "EPmNtSbK0VEX9JMyTeLr8WLLa"
consumer_secret = "j0bhW7iOnBuR9XcNEpKdLIyWmrAy2YMhzbP3AIZabL3EmtmJmv"
access_token = "1149105082442514434-amuNTlY7ef90gLOpIl1lW0Jfkx5NFz"
access_token_secret = "O8OZ7dkO6zoyCXRu2cnjuEDLZO68HuAn81XHxPUeYlIMS"

dirName = 'data'
file_path = dirName + '/twitter_data1.txt'
file = open(file_path, 'a')
file_num = 1
doneCrawling = False

class twitterListener(StreamListener):

    def on_data(self, data):
    	global file
    	global file_num
    	global doneCrawling

    	#2GB data reached
    	if (file_num >= 200):
    		print("2GB of data reached")
    		doneCrawling = True
    		return False

    	if (file.tell() >= 10000000):
    		file.close()
    		file_num += 1
    		file_path = dirName + '/twitter_data' + str(file_num) + '.txt'
    		file = open(file_path, 'a')

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
			l = twitterListener()
			auth = OAuthHandler(consumer_key, consumer_secret)
			auth.set_access_token(access_token, access_token_secret)
			stream = Stream(auth, l)

			stream.filter(locations=[-124.48, 32.53, -114.13, 42.01])
		except Exception as e:
			print("Exception error: " + e)
			time.sleep(30)
			print("Resuming crawling")
			pass
	f.close()
