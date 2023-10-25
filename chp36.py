# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 02:24:56 2023

@author: darel
"""
#Chapter 3
#Exercise 6: Shrinking Guest List
invitees = ["loko", "joko", "kiko"]# Make a list of who you would like to have dinner with.
print(" i cannot more than 3 so i can only invite only 2 people for dinner.")# Print an announcement that only two people are invited.
while len(invitees) > 2:# To remove guests one at a time and print messages, use pop().
    removed_guest = invitees.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")
for invitee in invitees:# Print notes for the final two visitors.
    print(f"Dear {invitee}, you're still invited to dinner.")
del invitees[:]## To clear the list, use del.
print("Guest list is now empty:", invitees)# Print the empty list
