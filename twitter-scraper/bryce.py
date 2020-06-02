from twitter_scraper import get_tweets
import pandas as pd
import numpy as np
tweets = []
twitter_account_list = pd.read_csv('twitter_accounts.csv')
for profile in twitter_account_list:
    print(profile)
    for tweet in get_tweets(profile, pages=10):
        tweets.append(tweet)
np.savetxt("tweets.csv", tweets, delimiter=",", fmt='%s')