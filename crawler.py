import os
import json
import pandas
import pandas as pd
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key = "EPmNtSbK0VEX9JMyTeLr8WLLa"
consumer_secret = "j0bhW7iOnBuR9XcNEpKdLIyWmrAy2YMhzbP3AIZabL3EmtmJmv"
access_token = "1149105082442514434-amuNTlY7ef90gLOpIl1lW0Jfkx5NFz"
access_token_secret = "O8OZ7dkO6zoyCXRu2cnjuEDLZO68HuAn81XHxPUeYlIMS"

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(locations=[-124.48,32.53,-114.13,42.01])