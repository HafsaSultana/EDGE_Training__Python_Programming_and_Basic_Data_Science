# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:27:21 2024

@author: Hafsa
"""

def square(a):
    return a*2


def add(a,b):
    print("addition")
    return(a+b)


import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
