# Script to selectively delete tweets and favs

This script deletes all tweets and/or favs of a Twitter account. I borrowed heavily from [this post](https://www.mathewinkson.com/2015/03/delete-old-tweets-selectively-using-python-and-tweepy) for this script. 

## Requirements

* A Twitter developer account. You can apply for one [here](https://developer.twitter.com/en/apply/user.html).
* A file named ```keys.py``` containing the credentials of your developer account:

```python
API_KEY='XXXXXXXXX'
API_SECRET='XXXXXXXXXX'
ACCESS_TOKEN='XXXXXXXX'
ACCESS_SECRET='XXXXXXXXXXX'
```

* The ```tweepy``` python library.

## Use

Add the ID of any tweet you'd like to keep to the ```keep_tweets.py``` file like this:
```python
TWEET_IDS=[1292155096923504640, 1354904079940558848]
```
The script has the following arguments:
* ```-t```: Delete tweets
* ```-f```: Delete favorites
* ```-d```: Date in yyyy-mm-dd format. The script will not delete all tweets and/or favs that were created at or after that date (if no date is specified the script will delete all tweets and favs)
* ```-v```: Verbose mode

For example, if you want to delete all tweets and favorites created before Jan 1st, 2021, write in the command line:
```
python delete_tweets.py -t -f -d 2021-01-01
```
