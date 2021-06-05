# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:53:40 2020

@author: Mahabaleshwara.Bairi
"""
print ("Return False if not all items in set x are present in set y:")
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}

print(x)
print(y)
z = x.issubset(y)

print(z)