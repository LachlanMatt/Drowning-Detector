# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 14:17:10 2021

@author: Lachlan
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:27:01 2021

@author: Lachlan
"""

import cv2
import os
import re
import _thread
import threading
import time
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

def extract( filename ):
    print("Starting v2 %s" % filename)
    foldername = filename.split('.')[0]
    number = 0
    for name in foldername.split(' '):
        if re.search(r".*[0-9]+.*", name) != None:
            number = name
            # print (number)
            break
    foldername = foldername.split(' ')[0] + "_" + str(number)
    print (foldername, filename)
    # print (filename)
    vidcap = cv2.VideoCapture(inputPath+filename)
    success,image = vidcap.read()
    count = 0
    outputpath = "%s%s/" % (inputPath, foldername)
    for i in range(3000000):
        if(i%1000000==0):
            print("for %s done %d\n" % (foldername, i))
    # try:
    #     os.mkdir(outputpath)
    #     os.mkdir(outputpath+"10x/")
    #     while success:
    #         cv2.imwrite("%s%s_f%d.jpg" % (outputpath, foldername, count), image)
    #         if count%10==0:
    #             cv2.imwrite("%s10x/%s_f%d.jpg" % (outputpath, foldername, count), image)
    #         success,image = vidcap.read()
    #         # print('Read a new fream: ', success)
    #         count += 1
    #     print("%s%s_f%d.jpg" % (outputpath, foldername, count))
    #     print("finished %s" % filename)
    #     print("\n")
    # except:
    #     print("path already exists for %s" % filename)
    # break
initialThreads = threading.activeCount()
print ("starting num threads is %d" % initialThreads )
for filename in importPics():
    try:
        _thread.start_new_thread( extract, ( filename, ) )
        print("Starting thread for %s" % filename)
    except Exception as inst:
        print ("Exception", inst, filename)
    
while threading.activeCount()>initialThreads:
    print("Waiting, Num threads remaining: %d" %  threading.activeCount())
    time.sleep(5)
    
print("finished")
    