# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 12:18:08 2019

@author: Saurabh
"""

s="02:05:10PM"
def time_conversion(s):
    if(s[-2:]=='AM' and s[:2]=='12'):
        return '00'+s[2:-2]
    elif(s[-2:]=='AM'):
        return s[:-2]
    if(s[-2:]=='PM' and s[:2]=='12'):
        return s[:-2]
    else:
        return str(int(s[:2])+12) + s[2:-2]