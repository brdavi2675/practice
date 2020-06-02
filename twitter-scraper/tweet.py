from twitter_scraper import get_tweets

for tweet in get_tweets('realDonaldTrump',pages=10):
    print(tweet['text'])
