# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 22:34:17 2019

@author: Saurabh
"""
grades=[]
n=int(input())
for _ in range(n):
    gr=int(input())
    grades.append(gr)
for grade in grades:
    if grade >= 38:
        if (grade % 5 > 2):
            grade += 5 - (grade % 5)
    print(grade)