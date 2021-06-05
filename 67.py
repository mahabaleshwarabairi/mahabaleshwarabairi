# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:15:24 2020

@author: Mahabaleshwara.Bairi
"""

import shelve
s=shelve.open("c")
s["India"]="DELHI"
s["Russia"]='Moscow'
for key in s:
    print (key)
s.close()
