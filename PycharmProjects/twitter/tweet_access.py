import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable

# Replace these values with our own twitter app settings
CONSUMER_KEY = 'MTaRhqhZU4ysFVOxxEgT35gPP'
CONSUMER_SECRET = 'BMVMybPpe2YcPCdOhIL2eK3yk3YoK6RD2S6qmenS4zAvHErntg'
OAUTH_TOKEN = '2507131836-ctbamJYSGXPK68jYt3k2JnXqhsdbdr4Wvk5XtCS'
OAUTH_TOKEN_SECRET = 'QlXneemNfdfDgqaXqyq27TvJdR6OJjBATdIfq0f4xK05h'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 50
query = 'Weather'

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name']
                for status in results
                for mention in status._json['entities']['user_mentions']]

hashtags = [hashtag['text']
            for status in results
            for hashtag in status._json['entities']['hashtags']]

words = [w for t in status_texts
         for w in t.split()]

for label, data in (('Text', status_texts),
                    ('Screen Name', screen_names),
                    ('Word', words)):
    table = PrettyTable(field_names=[label, 'Count'])
    counter = Counter(data)
    [ table.add_row(entry) for entry in counter.most_common()[:10] ]
    table.align[label], table.align['Count'] = 'l', 'r' # align the columns
    print table


    def get_lexical_diversity(items):
        return 1.0 * len(set(items)) / len(items)


    def get_average_words(tweets):
        total_words = sum([len(tweet.split()) for tweet in tweets])
        return 1.0 * total_words / len(tweets)


    print "Average words: %s" % get_average_words(status_texts)
    print "Word Diversity: %s" % get_lexical_diversity(words)
    print "Screen Name Diversity: %s" % get_lexical_diversity(screen_names)
    print "HashTag Diversity: %s" % get_lexical_diversity(hashtags)