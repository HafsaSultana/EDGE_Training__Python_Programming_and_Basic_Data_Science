# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:29:02 2024

@author: Hafsa
"""

'''
# 0714-02-cse-2201
c = input("Write: ")
r = c.replace('-', ' ')
print(r)


l= [1,2,3,2,4,1,5,6,7,6,4]
q = set(l)

x=4.555555
print("%.2f" % ( x)) 


x=5
y=8
print("Geeks :{0}, Portal :{1}".format(x,y))

'''
import random
import numpy as np

student = np.random.randint(100,150, size=4)
print(student)

print(student*10)


x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])
z = np.array([6, 7, 8, 9, 10])

temp = np.any(x==y)
print(temp)
temp = np.all(x==y)
print(temp)
temp = np.where(x<=3)
print(temp)






