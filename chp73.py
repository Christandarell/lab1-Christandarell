# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 05:20:23 2023

@author: darel
"""
#Chapter 7
#Exercise 3: T-Shirt
def make_shirt(size, message):
    print(f"Making a shirt of size {size} with the message: {message}")

# Call the function using positional arguments
make_shirt("medium", "Hello, World!")

# Call the function using keyword arguments
make_shirt(size="large", message="Python Programmer")
