# Code is modified from online resources
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json


access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


# Print out tweets
class StdOutListener(StreamListener):

    def on_data(self, data):
        # Extracting hashtags from json object
        hashtags = json.loads(data)['entities']['hashtags']
        for entry in hashtags:
            print(entry['text'])
        # Extrating URL from json object
        urls = json.loads(data)['entities']['urls']
        for url in urls:
            print(url['expanded_url'])
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # Connecting to Twitter
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # Filtering tweets by nba keyword and the English language
    stream.filter(languages=['en'], track=['nba'])
