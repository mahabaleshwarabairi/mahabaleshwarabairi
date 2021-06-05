# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:21:11 2020

@author: Mahabaleshwara.Bairi
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

r = y.difference(x)
print(x)
print (y)
print (" compare two sets x and y output is: x content  not there in y")
print(z)

print (" compare two sets x and y output is: y content  not there in x")
print(r)