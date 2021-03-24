#!/usr/bin/env python3
import video_upload as vu
import video_create as vc

def run(tweet_text):
    video_filename = "tmp_video.mp4"
    vc.create_video(video_filename, tweet_text)

    videoTweet = vu.VideoTweet(video_filename)
    videoTweet.upload_init()
    videoTweet.upload_append()
    videoTweet.upload_finalize()
    videoTweet.tweet(tweet_text)

def runGCP(request):
    run("Testing this musical tweet on GCP!")
    return "We processed your tweet!"

if __name__ == "__main__":
    run("Testing this musical tweet!")
