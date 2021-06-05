# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:05:58 2020

@author: Mahabaleshwara.Bairi
"""

import urllib.request 
request_url = urllib.request.urlopen('https://www.geeksforgeeks.org/') 
print(request_url.read()) 