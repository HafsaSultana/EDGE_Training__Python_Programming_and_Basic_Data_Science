# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:41:24 2024

@author: Hafsa

"""

import numpy as np

#Problem -1

def sum_corresponding_elements(arr1, arr2):
    
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    
    # print(len(arr1))
    # print(len(arr2))
    
    max_length = max(len(arr1), len(arr2))
    
    #zero padding
    
    padded_arr1 = np.pad(arr1, (0, max_length - len(arr1)), 'constant')
    padded_arr2 = np.pad(arr2, (0, max_length - len(arr2)), 'constant')
    
    # print(padded_arr1)
    # print(padded_arr2)

    result = padded_arr1 + padded_arr2
        
    return result

# Example usage:
print("sum_corresponding_elements: ",sum_corresponding_elements([1, 2], [4, 5, 6]))
# Output: [5, 7, 9]



#Problem -2

def threshold_array(input_array):
    
    mean_value = np.mean(input_array)
   # print("mean_value---",mean_value)
    mask = input_array > mean_value
   # print("mask---",mask)
        
    result = np.where(mask, 1, 0)
    
    return result
    

# Example usage:
input_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("threshold_array: ",threshold_array(input_array))

'''
Sample Input:   Sample Output:
1 2 3           0 0 0
4 5 6           0 0 1
7 8 9           1 1 1
'''



