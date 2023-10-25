# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 02:31:07 2023

@author: darel
"""


places_to_visit = ["My house", "Philippines", "UK", "USA", "japan"]# Compile a list of destinations.
print("Original List:", places_to_visit)## Print the initial inventory.
print("Alphabetical Order:", sorted(places_to_visit))# To arrange a list alphabetically, use sorted() without changing the original
print("Reverse Alphabetical Order:", sorted(places_to_visit, reverse=True))## To reverse alphabetical order without changing the original list, use sorted().
places_to_visit.reverse()
print("Reversed List:", places_to_visit)
places_to_visit.reverse()
places_to_visit.sort()# For both reverse and alphabetical order, use sort().
print("Alphabetical Order (sorted):", places_to_visit)
places_to_visit.sort(reverse=True)
print("Reverse Alphabetical Order (sorted):", places_to_visit)
