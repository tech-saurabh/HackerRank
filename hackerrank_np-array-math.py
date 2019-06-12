# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:05:19 2019

@author: Saurabh
"""

N,M = map(int,input().split())
a = input().split()
b = input().split()
for i in ['add','subtract','multiply','divide','mod','power']:
    eval('numpy.{0}(input().split(),input().split())'.format(i))