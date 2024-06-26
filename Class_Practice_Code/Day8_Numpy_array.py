# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:31:46 2024

@author: Hafsa
"""
!pip install numpy
import numpy as np


arr = np.zeros((5,5), dtype=int)
print("zeros",arr)

arr = np.ones((7,7), dtype=int)
print("ones",arr)


arr = np.arange(0,20,2)
print("arange",arr)


arr = np.linspace(0,20,5)
print("linspace",arr)



arr = np.random.randint(3,20,( 5,5))
print("random",arr)

##1st row

print("1st row  = ",arr[0,:])
print("--1st row  = ",arr[0])

##2nd row

print("2nd row  = ",arr[1,:])
print("--2nd row  = ",arr[1])

##last row

print("last row  = ",arr[4,:])
print("--last row  = ",arr[4])

######################
##1st column

print("1st column  = ",arr[:,0])

##2nd column

print("2nd column  = ",arr[:,1])

##last column

print("last column  = ",arr[:,4])

################
##1st row 1st coloum

print("1st row 1st coloum = ",arr[0,0])

#2nd row 1st coloum

print("2nd row 1st coloum  = ",arr[1,0])

##last row

print("last row last coloum = ",arr[4,4])

