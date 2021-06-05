# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:44:21 2020

@author: Mahabaleshwara.Bairi
"""

import re
str ='Course location is london or paris!'### search patterns
mo=re.search(r"location.*(star|!|zurich)",str)
if mo:print (mo.group())