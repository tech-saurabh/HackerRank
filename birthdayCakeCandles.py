# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:58:53 2019

@author: Saurabh
"""

def birthdayCakeCandles(ar):
    b=max(ar)
    count=0
    for i in ar:
        if(i==b):
            count+=1
    return(count)        
