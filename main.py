import os
from datetime import datetime
from mySpreadsheet import getTweet
from myTwitter import postTweet

tweet_message = getTweet()
#print(tweet_message)

tweet_status = postTweet(tweet_message)
#print(tweet_status)
