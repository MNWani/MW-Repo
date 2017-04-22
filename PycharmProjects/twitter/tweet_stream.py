from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

CONSUMER_KEY = 'MTaRhqhZU4ysFVOxxEgT35gPP'
CONSUMER_SECRET = 'BMVMybPpe2YcPCdOhIL2eK3yk3YoK6RD2S6qmenS4zAvHErntg'
OAUTH_TOKEN = '2507131836-ctbamJYSGXPK68jYt3k2JnXqhsdbdr4Wvk5XtCS'
OAUTH_TOKEN_SECRET = 'QlXneemNfdfDgqaXqyq27TvJdR6OJjBATdIfq0f4xK05h'

keyword_list = ['python', 'java', 'c#', 'ruby']  # track list


class MyStreamListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print "Failed on_data: %s" % str(e)
        return True

    def on_error(self, status):
        print status
        return True


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)