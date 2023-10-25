# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 02:16:15 2023

@author: darel
"""
#chapter 3
#Exercise 4: Guest List
invitees = ["kokie", "Amper", "Vary"]# Make a list of who you would like to have dinner with.
for invitee in invitees:# Send original invitations for dinner.
    if invitee == "amper":
        print(f"Dear {invitee}, I'd love to have a dinner with you and discuss your groundbreaking theories.")
    elif invitee == "Chubby":
        print(f"Dear {invitee}, I admire your contributions to science and would be honored to have you for dinner.")
    elif invitee == "kokie":
        print(f"Dear {invitee}, your artistic talents and inventions fascinate me. Let's dine and talk about your works.")
