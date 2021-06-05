# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:38:36 2020

@author: Mahabaleshwara.Bairi
"""

C={'A',"B","C"}
J={'A','D','E'}
print ("C is checking with J and display differance in J")
D=J.difference(C) ##different in two set
print (D)
print ("J is checking with C and display differance in D")
E=C.difference(D) ##different in two set
print (E)
C.discard("P")##no error if its not there 
#C.remove("P") #####error if content s not there 
print (C)
