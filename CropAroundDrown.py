# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:27:01 2021

@author: Lachlan
"""

import cv2
import os
import re
import time
timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
inputPath = "./RawYoutubeVideos/MaxResAudio/"
outputPath = "./CroppedImages/"+timestr+"/"
inputType = ["mp4", "jpg", "jpeg", "png"]
multiple = 10


def importFolders(inputPath):
    arr = os.listdir(inputPath)
    # return arr
    
    # print(arr)
    fileList = []
    fileType = inputType[0]
    for t in inputType:
        fileType = fileType+"|"+t
    for a in arr:
        if (re.match(".+\.("+fileType+")$",a)):
            pass
        elif (re.match(".+\_[0-9]*$",a)):
            fileList.append(a)
    return fileList

def importPics(inputPath):
    arr = os.listdir(inputPath)
    # print(arr)
    fileList = []
    fileType = inputType[0]
    for t in inputType:
        fileType = fileType+"|"+t
    for a in arr:
        if (re.match(".+[0-9]*0\.("+fileType+")$",a)):
            fileList.append(a)
    return fileList

os.mkdir(outputPath)
for foldername in importFolders(inputPath):
    
    
    print(foldername)
    print(inputPath+foldername)
    
    for filename in importPics(inputPath+foldername):
        print(filename)
        print(inputPath+foldername+"/"+filename)
        print(outputPath+filename)
        img = cv2.imread(inputPath+foldername+"/"+filename)
        w, h, c = img.shape
        print(w, h, c)
        for num in range(9):
            w1 = int( (0+int(num/3)) *w/4)
            w2 = int( (2+int(num/3)) *w/4)
            h1 = int( (0+int(num%3)) *h/4)
            h2 = int( (2+int(num%3)) *h/4)
            print(num, w1, w2, h1, h2)
            crop = img[w1:w2, h1:h2]
            # cv2.imshow("Piccy pic", img)
            # cv2.imshow("Piccy pic", crop)
            cv2.imwrite(outputPath+filename, img)
            cv2.imwrite(outputPath+"Crop"+str(num)+"_"+filename, crop)
        
        
        
        break
    
    break

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
