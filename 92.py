# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:28:27 2020

@author: Mahabaleshwara.Bairi
"""
print ("Remove the items that are present in both sets, AND insert the items that is not present in both sets:")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)