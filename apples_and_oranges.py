# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 12:22:17 2019

@author: Saurabh
"""

s,t,a,b,m,n=(7,11,5,15,3,2)
apples=[-2,2,1]
oranges=[5,-6]
apple,orange=(0,0)
for i in apples:
    if(s<=(a+i)<=t):
        apple+=1
for j in oranges:            
    if(s<=(b+j)<=t):
        orange+=1
print(apple,orange,sep="\n")