# play_youtube_video.py

import pywhatkit


def play_youtube_video(video_name):
    print(f"Attempting to play video: {video_name}")
    pywhatkit.playonyt(video_name)
    print("Done")

video_name = input("Enter the name of the video: ")
play_youtube_video(video_name)
