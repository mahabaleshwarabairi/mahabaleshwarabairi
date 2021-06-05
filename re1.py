# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:13:28 2020

@author: Mahabaleshwara.Bairi
"""

import re
a="Mascow is a beautiful city"
if re.search('i*',a):
    print ('Got it \n')
if re.search('I*',a):
    print ("Hit it \n")
if re.search('s+',a):
    print ("Found s \n")
if re.search ('l?',a):
    print (" FOund L \n")
if re.search('^M',a):
    print ('Found M \n')
if re.search('y$',a):
    print ("found Y ")
