# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 01:57:42 2023

@author: darel
"""

#Chapter 2
#xercise 5: USB Shopper
usb_stick_cost = 3# The total budget and the price of each USB stick
total_budget = 171
num_usb_sticks = total_budget // usb_stick_cost# Determine how many USB sticks she can purchase.
remaining_budget = total_budget % usb_stick_cost# Determine how much money is left over after buying USB stic
print("Number of USB sticks she can buy:", num_usb_sticks)# Show the outcome
print("Remaining pounds after purchase:", remaining_budget)
