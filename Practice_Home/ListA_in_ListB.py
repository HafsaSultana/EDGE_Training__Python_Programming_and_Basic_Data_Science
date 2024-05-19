# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:15:55 2024

@author: Hafsa
"""

l1= ["111","222",'333']
l2= ['jack','mili','lili',"111","222",'333']

flag=0

for i in l1:
    if i not in l2:
        flag=1
        print("Nope")
        break
    
if flag==0:
    print("Yes")
        
        
    