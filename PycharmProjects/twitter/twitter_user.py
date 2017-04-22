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

user = api.get_user('@madonna')

print user.screen_name
print user.followers_count

for friend in user.friends():
    print
    print friend.screen_name
    print friend.followers_count