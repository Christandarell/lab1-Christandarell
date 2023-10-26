# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 04:39:21 2023

@author: darel
"""
#Chapter 5
pets = [
    {"kind": "Dinosaur", "owner": "koki"},#Compile a list of dictionaries with images of various pets.
    {"kind": "Giraffe", "owner": "kevin"},
    {"kind": "Shark", "owner": "Kolokoy"},
    {"kind": "9 tails fox", "owner": "Mako"}
]
for pet in pets:
    print(f"Kind of Animal: {pet['kind']}")#Iterate through the list and print each pet's details.
    print(f"Owner's Name: {pet['owner']}")
    print() # A blank line to divide the details for each pet
