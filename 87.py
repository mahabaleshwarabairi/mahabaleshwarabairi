# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:45:26 2020

@author: Mahabaleshwara.Bairi
"""
print ("Return True if no items in set x is present in set y:")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.isdisjoint(y)

print(z)