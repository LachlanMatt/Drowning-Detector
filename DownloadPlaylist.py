# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:51:54 2021

@author: Lachlan
"""

from pytube import YouTube
from pytube import Playlist

playlist = Playlist("https://www.youtube.com/playlist?list=PLPpbDsYV8nKWvibJZm4A4GtmNBGJZphyq").video_urls

for video_link in playlist:
  
    try:
        YouTube(video_link).streams.first().download()
    
    except:
        print(video_link + " unavailable")