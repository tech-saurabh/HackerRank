# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 12:38:23 2019

@author: Saurabh
"""
lenA, lenB = map(int, input().split())
setA = list(map(int, input().split()))
setB = list(map(int, input().split()))

maxA = max(setA)
minB = min(setB)
count = 0
for num in range(maxA, minB + 1):
    left = all([num % numA == 0 for numA in setA])
    right = all([numB % num == 0 for numB in setB])
    count += left*right
print(count)