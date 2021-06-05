# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:00:18 2020

@author: Mahabaleshwara.Bairi
"""

while True:
    gty=input("Quantity Sold:")
    if int(gty)==0:
        print ("Enter Quantity more then zero")
        break
    price=input("Unit Price")
    sales=0
    sales=int(gty) * int(price)
    print ("Sales Value :",sales)
    