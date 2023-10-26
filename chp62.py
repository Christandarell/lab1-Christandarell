# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 05:00:07 2023

@author: darel
"""

#Chapter 6
#Exercise 2: Movie Tickets
while True:
    age = input("Please enter your age (or 'quit' to exit): ")

    if age.lower() == 'quit':
        break  # Exit the loop if 'quit' is entered

    age = int(age)  # Convert the input to an integer

    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
