# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:50:17 2020

@author: Mahabaleshwara.Bairi
"""
print ("Return True if all items set x are present in set y:")
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(x)
print(y)
print(z)