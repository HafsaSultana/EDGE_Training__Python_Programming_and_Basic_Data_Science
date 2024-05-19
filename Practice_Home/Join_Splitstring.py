# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:02:49 2024

@author: Hafsa
"""


def join_str(l): 
    x= l.join('_')
    return x
        
'''
num_str=int(input("Enter your dataset column length: "))
string_list=[]
for i in range(0,num_str):
    string= input("Enter your data: ")
    string_list.append(string)
'''    

string_list = ['i', 'am', '']
s=join_str(string_list)
print(s)


    
