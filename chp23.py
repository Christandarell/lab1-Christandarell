# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 01:51:23 2023

@author: darel
"""
#Chapter 2
#Exercise 3: Stripping Names 
name = "\t \nKokie Barokie \t\n"# Make use of a variable that contains whitespace
print("Name with Whitespace:", name)# Use whitespace to print the name.
print("Name with Left Stripping:", name.lstrip())## Use the functions strip(), rstrip(), and lstrip().
print("Name with Right Stripping:", name.rstrip())
print("Name with Stripping on Both Sides:", name.strip())
