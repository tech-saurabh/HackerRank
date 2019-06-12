# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:10:16 2019

@author: Saurabh
"""

def compareTriplets(a, b):
    Alice=0
    Bob=0
    for i in range(len(a)):
        for j in range(len(b)):
            if(i==j):
                if(a[i]>b[j]):
                    Alice+=1
                if(b[j]>a[i]):
                    Bob+=1        
    return(Alice,Bob)                             
