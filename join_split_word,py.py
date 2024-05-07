# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:52:25 2024

@author: Hafsa
"""

def join_split_word(value1,value2):
    string1 = value2.join(value1)
    print(string1)
    return string1.split(value2)
    
    
    
wordList = ["Hello", "World", "!"]
delimeter = ' '

print(join_split_word(wordList,delimeter )) 



