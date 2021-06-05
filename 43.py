# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:08:43 2020

@author: Mahabaleshwara.Bairi
"""
import string
def function1():
    print ("Cat Mews")
def function2():
    print ("Dog Barks")
def function3():
    print ("Bear Growls")
tokenDict={"cat":function1,"dog":function2,"bear":function3}
lines=["cat","bear","dog"]
for line in lines:
   functionTocall=tokenDict[line]
    
   functionTocall()
   