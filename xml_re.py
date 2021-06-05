# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:15:49 2020

@author: mahabaleshwara.bairi
"""

import requests
from xml.etree import ElementTree

response = requests.get('http://10.155.8.18:8080/MNP/MNPGetMDNDetails?msisdn=7558449852')

root = (ElementTree.fromstring(response.content))
#print (response.content)
print(root)
for child in root.iter('*'):
    print(child.tag)


for child in root.iter('CustomerCircleInfo'):
    print(child.tag, child.attrib)