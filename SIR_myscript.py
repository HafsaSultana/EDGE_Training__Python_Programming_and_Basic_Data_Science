# -*- coding: utf-8 -*-
"""
Created on Sun May  5 09:47:00 2024

@author: csepc2022
"""

#-------------------------------------
# file: myscript.py

def square(x):
    """square a number"""
    return x ** 2

for N in range(1, 4):
    print(N, "squared is", square(N))
    
    
  
"""    
## execution time line-wise  
    
%timeit L = [n ** 2 for n in range(1000)]

  
## execution time cellwise 

%%timeit
L = []
for n in range(1000):
    L.append(n ** 2)
    
## Input Output History 
 
    
In [1]: import math

In [2]: math.sin(2)
Out[2]: 0.9092974268256817

In [3]: math.cos(2)

In [4]: print(In)
['', 'import math', 'math.sin(2)', 'math.cos(2)', 'print(In)']

In [5]: Out
Out[5]: {2: 0.9092974268256817, 3: -0.4161468365471424}

"""