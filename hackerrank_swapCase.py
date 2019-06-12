# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:59:11 2019

@author: Saurabh
"""

def swap_case(s): #change lower to upper case and vice versa
    b=""
    for i in s:
        if(i.isupper()):
            b=b+i.lower()
        elif(i.islower()):
            b=b+i.upper()
        else:
            b=b+i

    return(b)