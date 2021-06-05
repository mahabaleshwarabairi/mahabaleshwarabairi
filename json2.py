# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:41:23 2020

@author: Mahabaleshwara.Bairi
"""
import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)