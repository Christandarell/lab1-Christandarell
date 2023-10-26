# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 03:35:29 2023

@author: darel
"""

#Exercise 4: Stages of Life 
# Get the person's age as input
age = int(input("Enter the person's age: "))

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")


