import json
import tweepy
from tweepy import OAuthHandler


# Replace these values with our own twitter app settings
CONSUMER_KEY = 'MTaRhqhZU4ysFVOxxEgT35gPP'
CONSUMER_SECRET = 'BMVMybPpe2YcPCdOhIL2eK3yk3YoK6RD2S6qmenS4zAvHErntg'
OAUTH_TOKEN = '2507131836-ctbamJYSGXPK68jYt3k2JnXqhsdbdr4Wvk5XtCS'
OAUTH_TOKEN_SECRET = 'QlXneemNfdfDgqaXqyq27TvJdR6OJjBATdIfq0f4xK05h'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418


dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

dub_trends_set = set([trend['name']
                      for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                      for trend in lon_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set)

print common_trends
