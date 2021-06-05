# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:26:23 2020

@author: Mahabaleshwara.Bairi
"""
##Remove the items that exist in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

y.difference_update(x)

print(x)
print(y)

