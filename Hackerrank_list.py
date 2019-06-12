# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script """

N=int(input())
l=[1,2,3,4]
for _ in range(N):
    s=input().split()
    cmd,args=s[0],tuple(map(int,(s[1:])))
    if(cmd=='print'):
        print(l)
    else:
        eval('l.{0}{1}'.format(cmd,args))     
    
    