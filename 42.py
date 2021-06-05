# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:52:10 2020

@author: Mahabaleshwara.Bairi
"""

def town(capital):
    print ("Capital of TN :",capital)
    capital="Chennai" ##local
    print ("Now its :",capital)
    
capital='MADRAS' ###global
town(capital)
print ("Still its :",capital)