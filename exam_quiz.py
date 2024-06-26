# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:18:15 2024

@author: Hafsa
"""
import pandas as pd
import random

pd.__version__


data = pd.Series([0.25, 0.5, 0.75, 1.0])



random_num = random.randint(1, 10)

def func1(a,b):
    return a/b

def func2(x):
    a=x
    b=x-1
    return func1(a,b)


    