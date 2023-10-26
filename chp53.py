# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 04:32:53 2023

@author: darel
"""
#Chapter 5
#Exercise 3: Glossary 2
# Create a glossary with programming terms and their meanings
glossary = {
    "Variable": "A named storage location in a program's memory for storing data.",
    "Function": "A reusable block of code that performs a specific task.",
    "Loop": "A control structure that repeats a set of instructions as long as a certain condition is met.",
    "String": "A data type used to represent text, typically enclosed in single or double quotes.",
    "List": "A collection of ordered and mutable elements in Python.",
    "Dictionary": "A collection of key-value pairs in Python.",
    "Boolean": "A data type that represents one of two possible values: True or False.",
    "Tuple": "An ordered and immutable collection of elements in Python.",
    "Module": "A file containing Python definitions and statements.",
    "Method": "A function associated with an object or a class."
}

# Loop through the glossary and print each term and its meaning
for term, meaning in glossary.items():
    print(f"{term}:\n{meaning}\n")
