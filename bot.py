#!/usr/bin/env python3
import os
import tweepy
from secrets import *
from time import gmtime, strftime

# ====== Individual bot configuration ==========================
bot_username = 'hatelbot'

def create_tweet():
    """Create the text of the tweet you want to send."""
    # Replace this with your code!
    text = "Testing how to create twitter bots."
    return text


def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        print(e)
    else:
        print("Tweeted: " + text)

if __name__ == "__main__":
    tweet_text = create_tweet()
    tweet(tweet_text)
