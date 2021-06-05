# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:36:14 2020

@author: Mahabaleshwara.Bairi
"""

import re
s='a,b,,,c,,d  e'
r=re.split('[, ]+',s)
print (r)