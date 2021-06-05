# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:23:43 2020

@author: Mahabaleshwara.Bairi
"""

import urllib.request 
import urllib.parse 
import re 
   
url = 'https://www.geeksforgeeks.org/'
values = {'s':'python programming', 
          'submit':'search'} 
   
data = urllib.parse.urlencode(values) 
data = data.encode('utf-8') 
req = urllib.request.Request(url, data) 
resp = urllib.request.urlopen(req) 
respData = resp.read() 
   
paragraphs = re.findall(r'<p>(.*?)</p>',str(respData)) 
   
for eachP in paragraphs: 
    print(eachP) 