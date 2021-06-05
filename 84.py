# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:40:49 2020

@author: Mahabaleshwara.Bairi
"""
print ("Compare 3 sets, and return a set with items that is present in all 3 sets:")
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
print(x)
print(y)
print(z)
x.intersection_update(y, z)

print(x)
print(y)
print(z)


x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}

x1.intersection_update(y1)

print(x1)
