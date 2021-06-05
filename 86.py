# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:35:07 2020

@author: Mahabaleshwara.Bairi
"""
print ("Remove the items that is not present in both x, and set y:")
x = {"apple", "banana", "cherry","kiwi"}
print (x)

y = {"google", "microsoft", "apple","kiwi"}
print (y)
x.intersection_update(y)

print(x)