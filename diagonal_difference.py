# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:10:49 2019

@author: Saurabh
"""

def diagonalDifference(arr):
    a,b=(0,0)
    for i in range(n): #n is the row/column size of square matrix
        a=a + arr[i][i]
        b=b + arr[i][n-i-1]
    return(abs(a-b))    
