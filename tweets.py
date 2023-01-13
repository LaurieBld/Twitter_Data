# Importation des modules nécéssaires
import tweepy
import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt
# On importera plus tard Cassandra BDD NO SQL car actuellement cela ne fonctionne pas 



# Dev twitter portal
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
bearer_token = ""
# On s'id avec Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# On cherche les tweets contenant "concerts" par hashtags
client = tweepy.Client(consumer_key= consumer_key,consumer_secret= consumer_secret,access_token= access_token,access_token_secret= access_token_secret, bearer_token=bearer_token)
query = 'concerts'
tweets = client.search_recent_tweets(query=query, max_results=10)
for tweet in tweets.data:
    print(tweet.text, tweet.user.screen_name)


