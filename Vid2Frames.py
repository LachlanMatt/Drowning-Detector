# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:27:01 2021

@author: Lachlan
"""

import cv2
import os
import re
inputPath = "./RawYoutubeVideos/MaxResAudio/"
#outputpath = "./RawYoutubeVideos/MaxResAudio/"
inputType = ["mp4"]


def importPics():
    arr = os.listdir(inputPath)
    # print(arr)
    fileList = []
    fileType = inputType[0]
    for t in inputType:
        fileType = fileType+"|"+t
    for a in arr:
        if (re.match(".+\.("+fileType+")$",a)):
            fileList.append(a)
    return fileList

for filename in importPics():
    foldername = filename.split('.')[0]
    number = 0
    for name in foldername.split(' '):
        if re.search(r".*[0-9]+.*", name) != None:
            number = name
            print (number)
            break
    foldername = foldername.split(' ')[0] + "_" + str(number)
    print (foldername)
    print(filename)
    vidcap = cv2.VideoCapture(inputPath+filename)
    success,image = vidcap.read()
    count = 0
    outputpath = "%s%s/" % (inputPath, foldername)
    try:
        os.mkdir(outputpath)
        os.mkdir(outputpath+"10x/")
        while success:
            cv2.imwrite("%s%s_f%d.jpg" % (outputpath, foldername, count), image)
            if count%10==0:
                cv2.imwrite("%s10x/%s_f%d.jpg" % (outputpath, foldername, count), image)
            success,image = vidcap.read()
            # print('Read a new fream: ', success)
            count += 1
        print("%s%s_f%d.jpg" % (outputpath, foldername, count))
        print("\n")
    except:
        print("path already exists")
    # break
