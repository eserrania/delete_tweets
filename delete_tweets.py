import tweepy
import argparse
from datetime import datetime
from keys import *
from keep_tweets import *


# Autenticar en Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)


def delete_timeline(date, delete_tweets=True, delete_likes=True, verbose=False):
	if delete_tweets:
	    timeline = tweepy.Cursor(api.user_timeline, wait_on_rate_limit=True).items()
	    tweet_counter = 0
	    for tweet in timeline:
	        if (tweet.id not in TWEET_IDS) & (tweet.created_at < date):
	            if verbose:
	                print('Deleting tweet: "%s"' % tweet.text)
	            api.destroy_status(tweet.id)
	            tweet_counter += 1
	    print('Deleted %i tweets' % tweet_counter)

	if delete_likes:
	    likes = tweepy.Cursor(api.favorites, wait_on_rate_limit=True).items()
	    like_counter = 0
	    for tweet in likes:
	        if tweet.created_at <= date:
	            if verbose:
	                print('Unfavoring: "%s"' % tweet.text)
	            api.destroy_favorite(tweet.id)
	            like_counter += 1
	    print('Deleted %i likes' % like_counter)

if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	parser.add_argument(
		"-d", "--date", 
		help="Date in yyyy-mm-dd format",
		default=datetime.now().strftime('%Y-%m-%d'))
	'''

	parser.add_argument(
		"-t", "--tweets", 
		help="Delete tweets",
		default=datetime.now().strftime('%Y-%m-%d'))

	parser.add_argument(
		"-f", "--favs", 
		help="Delete favorites",
		default=datetime.now().strftime('%Y-%m-%d'))
	'''

	args = parser.parse_args()

	delete_timeline(date=datetime.strptime(args.date, '%Y-%m-%d'))
    
  
   