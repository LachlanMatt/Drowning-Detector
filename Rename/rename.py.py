# -*- coding: utf-8 -*-
"""
Created on Thu May 13 09:26:37 2021

@author: Lachlan
"""

import os

count = 0

for i in os.listdir():
    os.rename(i,str(count)+ '.'+ i.split('.')[-1])
    count+=1