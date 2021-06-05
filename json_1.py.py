# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:40:35 2020

@author: Mahabaleshwara.Bairi
"""

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])