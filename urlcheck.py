# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:45:58 2020

@author: Mahabaleshwara.Bairi
"""

import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
print (html)