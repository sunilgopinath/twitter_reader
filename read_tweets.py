import sys
import ConfigParser
import oauth2 as oauth
import json
from collections import OrderedDict

class UrlsFromHashtags:
    
    def authenticate_client(self, consumer_key, consumer_secret):
        ''' reads the config file to find the twitter access tokens '''
        
        parser = ConfigParser.SafeConfigParser()
        config_values = parser.read('twitter.cfg')
        try:
            consumer = oauth.Consumer(key=consumer_key, 
                              secret=consumer_secret)
            access_token = oauth.Token(key=parser.get('token_access', 'access_key'), 
                               secret=parser.get('token_access', 'access_secret'))

            client = oauth.Client(consumer, access_token)
            return client
        except ConfigParser.NoSectionError:
            raise IOError
        
    def get_tweets(self, hashtag, client):
        ''' uses the twitter search api to find the latest tweets of
            given a hashtag.
                
            Query params from twitter api:
            count: we give it 100 per the exercise
            result_type: we need to give it recent to get the latest as default
                             is a mix of popular and latest
        '''
            
        search_endpoint = "https://api.twitter.com/1.1/search/tweets.json?q=%23"+hashtag+"&count=100&result_type=recent"                               
        response, data = client.request(search_endpoint)

        return json.loads(data)
