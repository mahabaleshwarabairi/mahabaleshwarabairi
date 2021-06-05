# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:47:54 2020

@author: Mahabaleshwara.Bairi
"""

def c(m,*others):
    """   accept variable 
    """
    print ("My Country is :",m)
    for contry in others:
            print ("Foreign Country is :",contry)
c('India','JAPAN','CHINA')
print (c.__doc__)
