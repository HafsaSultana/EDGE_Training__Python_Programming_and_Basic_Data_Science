# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:31:45 2024

@author: Hafsa
"""

import numpy as np
rng = np.random.default_rng(seed=1701)  # seed for reproducibility


x1 = rng.integers(10, size=6)  # one-dimensional array
x2 = rng.integers(10, size=(3, 4))  # two-dimensional array
x3 = rng.integers(10, size=(3, 4, 5))  # three-dimensional array

print("x1:   ",x1)
print("x2:   ",x2)
print("x3:   ",x3)

print("x3 ndim: ", x3.ndim)     # 3
print("x3 shape:", x3.shape)    #(3, 4, 5)
print("x3 size: ", x3.size)     #60
print("dtype:   ", x3.dtype)    #int64
print("x3_len",len(x1))



x1          #array([9, 4, 0, 3, 8, 6], dtype=int64)

x1[0]       #9    1st element

x1[4]       #8 ,  5th element


x1[-1]      #last element

x1[-2]      # 2nd last 


"""In a multidimensional array, items can be accessed using a comma-separated `(row, column)` tuple:"""

x2

x2[0, 0]  # 3  1st row , 1st column

x2[2, 0]  # 0  3rd row , 1st column

x2[2, -1]    # 9  3rd row , last column



"""Values can also be modified using any of the preceding index notation:"""

x2[0, 0] = 12
x2


"""Keep in mind that, unlike Python lists, NumPy arrays have a fixed type.
This means, for example, that if you attempt to insert a floating-point value into an integer array, the value will be silently truncated. Don't be caught unaware by this behavior!
"""

x1[0] = 3.14159  # this will be truncated!
x1


"""## Array Slicing: Accessing Subarrays"""


x1

x1[:3]  # first three elements

x1[3:]  # elements after index 3

x1[1:4]  # middle subarray

x1[::2]  # every second element

x1[1::2]  # every second element, starting at index 1

9.5/2
9.5//2
