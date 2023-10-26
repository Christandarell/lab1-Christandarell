# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 04:23:34 2023

@author: darel
"""

#chapter 5
#Exercise 2: Glossary 
# Create a glossary with programming terms and their meanings
# Create a glossary with programming terms and their meanings
glossary = {
    "Variable": "A named storage location in a program's memory for storing data.",
    "Function": "A reusable block of code that performs a specific task.",
    "Loop": "A control structure that repeats a set of instructions as long as a certain condition is met.",
    "String": "A data type used to represent text, typically enclosed in single or double quotes.",
    "List": "A collection of ordered and mutable elements in Python."
}

# Print each word and its meaning with blank lines in between
for term, meaning in glossary.items():
    print(f"{term}:\n{meaning}\n")
