# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:19:08 2024

@author: Hafsa
"""
import numpy as np
import array

# fixed array

L = list(range(10))
#L= ["a","b",True, 4]
A = array.array('i',L)
print(A)


A = np.array([1,3,6,2,8])
print(A)

A = np.array([1.5,3,6,2,8])
print(A)

A = np.array([1.5,3,6,2,8], dtype=np.float32)
print(A)

A = np.array([1.5,3,6,2,8], dtype=np.float32)
print(A)

# nested list result for multidimentional array

A=np.array([range(i,i+4) for i in [3,4,5,6]])
print(A)