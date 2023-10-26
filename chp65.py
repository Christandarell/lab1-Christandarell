# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 05:07:49 2023

@author: darel
"""

#chapt 6
#Exercise 5: No Pastrami
sandwich_orders = ["tuna", "turkey", "veggie", "ham", "chicken"]
finished_sandwiches = []
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
