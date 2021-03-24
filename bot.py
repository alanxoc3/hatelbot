#!/usr/bin/env python3
import os
import base64
import tweepy
import requests
import video_upload
from secrets import *
from time import gmtime, strftime

# ====== Individual bot configuration ==========================
bot_username = 'hatelbot'

def create_tweet():
    """Create the text of the tweet you want to send."""
    # Replace this with your code!
    text = "Testing how to create twitter bots."
    return text

def read_in_chunks(file_object, chunk_size):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)
    video_path = "my_video.mp4"
    vid_size = os.path.getsize(video_path)
    video_file = open(video_path, "rb") 
    video_data = video_file.read()

    # Send the tweet and log success or failure
    try:
        global payload, headers, rauth, init_upload_response, chunk_headers, chunk_payload, append_upload_response, file_param
        payload = {"media_category": "tweet_video", "command": "INIT", "total_bytes": vid_size, "media_type": "video/mp4"}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        rauth = auth.apply_auth()
        init_upload_response = requests.post("https://upload.twitter.com/1.1/media/upload.json", params=payload, headers=headers, auth=rauth)

        chunk_headers = {'Content-Type': 'multipart/form-data'}
        chunk_payload = {"command": "APPEND", "media_id": init_upload_response.json().get("media_id"), "segment_index": "0"}
        file_param = {video_path: video_data}
        append_upload_response = requests.post("https://upload.twitter.com/1.1/media/upload.json", files=file_param, params=chunk_payload, headers=chunk_headers, auth=auth.apply_auth())
    except tweepy.error.TweepError as e:
        print(e)
    else:
        print("Tweeted: " + text)

if __name__ == "__main__":
    tweet_text = create_tweet()
    tweet(tweet_text)
