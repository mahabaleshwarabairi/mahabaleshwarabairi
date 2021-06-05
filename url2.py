# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:07:27 2020

@author: Mahabaleshwara.Bairi
"""
import urllib
import urllib.parse

from urllib.parse import * parse_url = urlparse('https://www.geeksforgeeks.org / python-langtons-ant/') 
print(parse_url) 
print("\n") 
unparse_url = urlunparse(parse_url) 
print(unparse_url) 