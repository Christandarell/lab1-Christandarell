# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 02:19:16 2023

@author: darel
"""
#Chapter 3
#Exercise 5: Change Guest List
invitees = ["Bala", "koklo", "buko"]#Make a list of who you want to have over for dinner.
for invitee in invitees:# Print the original list's invitation messages.
    print(f"Dear {invitee}, I'd love to have a dinner with you and discuss your achievements.")
unavailable_guest = "koklo"#` Update the guest list to reflect their absence.
new_invitee = "jokosa"
invitees[invitees.index(unavailable_guest)] = new_invitee
for invitee in invitees:## Print invitations for the most recent list.
    print(f"Dear {invitee}, please join us for dinner.")
