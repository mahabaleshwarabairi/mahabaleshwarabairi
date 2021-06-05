# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:24:50 2020

@author: Mahabaleshwara.Bairi
"""

import datetime

x = datetime.datetime.now()
#print(x)

import datetime

x = datetime.datetime.now()

#print(x.year)

date_1=x.strftime("%d"+"-"+"%m"+"-"+"%Y")
print (date_1)

date_2=x.strftime("%d"+"-"+"%m"+"-"+"%Y"+"-"+"%I"+"-"+"%M"+"-"+"%S")
print (date_2)