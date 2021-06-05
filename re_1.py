# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:49:23 2020

@author: Mahabaleshwara.Bairi
"""

import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")


import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 


import re

print ("Split the string at every white-space character:")

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

print ("Split the string only at the first occurrence:")
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 2)
print(x[2])

print ("Replace every white-space character with the number 9:")
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


print ("Replace the first 2 occurrences:")
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)


print ("Do a search that will return a Match Object:")

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
