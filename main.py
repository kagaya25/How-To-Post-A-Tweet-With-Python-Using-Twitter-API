import tweepy
consumer_key = ""
consumer_secret = ""
consumer_token = ""
consumer_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(consumer_token,consumer_token_secret)
api = tweepy.API(auth)
api.update_status('I am posting tweet using Python and using tweepy TEST 2')
print("a tweet is posted")
