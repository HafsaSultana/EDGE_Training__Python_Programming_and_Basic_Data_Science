# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:36:56 2024

@author: Hafsa
"""
import random

random_num = random.randint(1, 10)

num = int(input("Enter your number: "))

if num==random_num:
    print("Your guess is correct.")
elif num>random_num:
    print("Your guess too high.")
else:
    print("Your guess is too low.")

    