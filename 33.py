# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:14:07 2020

@author: Mahabaleshwara.Bairi
"""

def interest(p,n,r):
    inter=0
    inter= (p* n*r)/100
    return inter

#p=200
#n=2
#r=3 
A=input ("Enter value for p:") 
p=int(A)
B= input ("Enter value for n:")  
n=int(B)
C=input ("Enter value for r:")  
r=int(C)
res=interest(p,n,r)
print (res)
