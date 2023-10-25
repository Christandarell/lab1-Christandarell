# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:37:17 2023

@author: darel
"""
#chapter 1
#Exercise 5: Compute area of Circle
import math
radius = float(input("Enter the radius of the circle: "))# Input: radius of the circle
area = math.pi * (radius ** 2)# Determine the area.
print(f"The area of the circle with radius {radius} is {area:.2f}")# print the radius
