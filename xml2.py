# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:49:16 2020

@author: mahabaleshwara.bairi
"""
import urllib2.request
import json
import xml.etree.ElementTree 
r = requests.get('http://10.155.8.18:8080/MNP/MNPGetMDNDetails?msisdn=7558449852')
root = ElementTree.fromstring(r.content)
for child in root.iter('*'):
    print(child.tag)