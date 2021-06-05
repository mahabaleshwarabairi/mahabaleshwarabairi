# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:42:04 2020

@author: Mahabaleshwara.Bairi
"""

def pickup(y):
    return y.isalnum() ####check alpha numaric key check 
val=["Ganesh","F12","12"]
out=list(filter(pickup,val))
print (out)