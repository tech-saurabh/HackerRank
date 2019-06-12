# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:43:25 2019

@author: Saurabh
"""

arr=[1,2,3,4,5]
minsum=0
maxsum=0
arr.sort()
for i in range(len(arr)-1):
    minsum=minsum+arr[i]
for i in range(1,len(arr)):
    maxsum=maxsum+arr[i]
print(minsum,maxsum)    
    