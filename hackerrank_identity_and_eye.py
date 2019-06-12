# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 18:33:47 2019

@author: Saurabh
"""

import numpy
numpy.set_printoptions(legacy='1.13') #used to change numpy version bcz of output mismatch
rowCol = list(map(int,input().split()))
rowCol.append(0)
rowCol=tuple(rowCol)
print(eval('numpy.{0}{1}'.format('eye',rowCol)))
