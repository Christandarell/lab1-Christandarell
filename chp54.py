# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 04:35:52 2023

@author: darel
"""

#Chapter 5 
#Exercise 4: Rivers
rivers = {#Make a dictionary of the nations that rivers flow through.
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Mississippi": "United States"
}
for river, country in rivers.items():#Loop to output sentences pertaining to every river
    print(f"The {river} runs through {country}.")
print("\nRivers:")#Print each river's name in a loop
for river in rivers.keys():
    print(river)
print("\nCountries:")# Loop to print each nation's name
for country in rivers.values():
    print(country)
