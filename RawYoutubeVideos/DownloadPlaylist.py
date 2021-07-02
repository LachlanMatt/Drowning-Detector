# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:51:54 2021

@author: Lachlan
"""

from pytube import YouTube
from pytube import Playlist
import ffmpeg

playlist = Playlist("https://www.youtube.com/playlist?list=PLgqwWmjSsNRzDOAmtyRc9K3fO-VMpE07C").video_urls

flip = False
for video_link in playlist:
    if (flip):
        continue
    #flip = True
    print(video_link)
    print("\n")
    try:
        # YouTube(video_link).streams.filter(progressive=True, mime_type="video/mp4").order_by('resolution').desc().first().download()
        print(YouTube(video_link).streams.filter(progressive=True, mime_type="video/mp4").order_by('resolution'))
        print(YouTube(video_link).streams.filter(progressive=True, mime_type="video/mp4").order_by('resolution').desc())
        print(YouTube(video_link).streams.filter(progressive=True, mime_type="video/mp4").order_by('resolution').desc().first())
        # YouTube(video_link).streams.first().download()
        # video_file = YouTube(video_link).streams.filter(mime_type="video/mp4").order_by('resolution').desc().first().download()
        # video_file = YouTube(video_link).streams.order_by('resolution').desc().first().download()
        # print(video_file)
        # print(YouTube(video_link))
        # print("\n")
        # print(YouTube(video_link).streams)
        # print("\n")
        # print(YouTube(video_link).streams.first())
        # print("\n")
        # print(YouTube(video_link).streams.filter(res="720p").order_by('resolution'))
        # print("\n")
        # print(YouTube(video_link).streams.filter(res="720p").order_by('resolution').desc())
        # print("\n")
        # print(YouTube(video_link).streams.filter(res="720p").order_by('resolution').desc().first())
        # print("\n")
        # print(YouTube(video_link).streams.filter(progressive=True, mime_type="video/mp4").order_by('resolution').desc())
        # print("\n")
        
        
        # audio_file = YouTube(video_link).streams.filter(only_audio=True).order_by('abr').desc().first().download(filename_prefix="audio_")
        # source_audio = ffmpeg.input(audio_file)
        # source_video = ffmpeg.input(video_file)
        # ffmpeg.concat(source_video, source_audio, v=1, a=1).output("video_name.mp4").run()
    
    except:
        print(video_link + " unavailable")
    
    break