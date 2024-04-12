# play_youtube_video.py

import pywhatkit


def play_youtube_video(video_name):
    print(f"Attempting to play video: {video_name}")
    pywhatkit.playonyt(video_name)
    print("Done")


play_youtube_video("The Truth About Learning Python in 2024")
