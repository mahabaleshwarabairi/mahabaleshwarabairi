# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:00:58 2020

@author: Mahabaleshwara.Bairi
"""

import re
p="2004-059-559"## this 
num=re.sub(r'#.*$', "",p)
print ("Phone Num:",num)
num1=re.sub(r'\D',"",p)
print ("Phone Num is:",num1)