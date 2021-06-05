# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:09:47 2020

@author: Mahabaleshwara.Bairi
"""
##unidue unorder,imutable
se=set("we are")
print (se)

bikes=set(("Honda","Suzuki","Honda")) ###set unique
print (bikes)

print("Adding value to list inside in set")
b=set(["A","B","C"])
print (b)
b.add("D")
print (b)
print("frozen set")##not allowed to add to set
e=frozenset(["A","B","C"])
print (e)
e.add("D")
print (e)
e.clear()##clear  set