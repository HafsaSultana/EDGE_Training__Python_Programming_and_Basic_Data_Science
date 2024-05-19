# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:44:24 2024

@author: Hafsa
"""
money_string= input("Enter your data: ")
print(money_string[5:8],money_string[len(money_string)-1])


#For full dataset
num_str=int(input("Enter your dataset column length: "))
dataset_list=[]
for i in range(0,num_str):
    string= input("Enter your data: ")
    dataset_list.append(string)
    

for string in dataset_list:
    print(string[5:8],string[len(string)-1])
    
    