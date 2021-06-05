# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:32:22 2020

@author: mahabaleshwara.bairi
"""

import urllib.request 
import json
import xml.etree.ElementTree 
r = requests.get('http://10.155.8.18:8080/MNP/MNPGetMDNDetails?msisdn=7558449852')
#print(request_url.read()) 
response=request_url.read()
print (response)
root = ElementTree.fromstring(r.content)
print (root)