#!/usr/bin/env python3
import video_upload as vu
import video_create as vc

def runGCP():
    video_filename = "a_video.mp4"
    tweet_text = "Testing this musical tweet on GCP!"
    vc.create_video(video_filename, tweet_text)

    videoTweet = vu.VideoTweet(video_filename)
    videoTweet.upload_init()
    videoTweet.upload_append()
    videoTweet.upload_finalize()
    videoTweet.tweet(tweet_text)

if __name__ == "__main__":
    video_filename = "a_video.mp4"
    tweet_text = "Testing this musical tweet!"
    vc.create_video(video_filename, tweet_text)

    videoTweet = vu.VideoTweet(video_filename)
    videoTweet.upload_init()
    videoTweet.upload_append()
    videoTweet.upload_finalize()
    videoTweet.tweet(tweet_text)
