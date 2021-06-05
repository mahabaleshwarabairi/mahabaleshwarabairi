# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:26:32 2020

@author: Mahabaleshwara.Bairi
"""
print ("Return a set that contains all items from both sets, except items that are present in both sets:")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)