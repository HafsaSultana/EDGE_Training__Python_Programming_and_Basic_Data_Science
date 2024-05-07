# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:04:11 2024

@author: Hafsa
"""

message = "  Hello world!  "
name = "Alice"
multilene_text =''' The shcool
is nice'''

print(multilene_text)

upper_msg = message.upper()

###*****Formatting
name="Bob"
age=20
formatted_text = f"Hello!, {name}, Your are {age} years old."

print(formatted_text)


###____title

magic  = ["aa", "bb", "ccc"]

for i in magic:
    print(i.title())
    print(f"{i.title()} is good.")
    

###___get

d=dict(a=2,b=2)
print(d['a'])
print(d.get('c','not found'))


for k in d.keys():
    print(k)
    
for k in d.values():
    print(k)
    
for k,v in d.items():
    print(k,v)



