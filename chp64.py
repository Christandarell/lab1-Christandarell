# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 05:06:10 2023

@author: darel
"""
#chapter 6
#Exercise 4: Deli
# Create a list of sandwich orders
sandwich_orders = ["tuna", "turkey", "veggie", "ham", "chicken"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Process each sandwich order
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
