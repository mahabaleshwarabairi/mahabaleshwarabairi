# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 23:08:25 2020

@author: Mahabaleshwara.Bairi
"""


username = input("Enter username:")

if not type(username) is str:
  raise TypeError("Only string are allowed")
else:
    print("Username is: " + username)