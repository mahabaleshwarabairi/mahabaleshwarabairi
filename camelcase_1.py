# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 23:04:24 2020

@author: Mahabaleshwara.Bairi
"""

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))