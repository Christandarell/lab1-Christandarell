# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 04:57:11 2023

@author: darel
"""
#Chapter 6
#Exercise 1: Pizza Toppings
toppings = []  # Create an empty list to store toppings

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    if topping.lower() == 'quit':
        break  # Exit the loop if 'quit' is entered
    else:
        toppings.append(topping)
        print(f"I'll add {topping} to your pizza.")
print("Your pizza with the following toppings is ready:")
for topping in toppings:
    print(topping)
