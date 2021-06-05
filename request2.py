# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:30:33 2020

@author: mahabaleshwara.bairi
"""

import urllib.request 
import json
number=input("Enter Number:")
request_url = urllib.request.urlopen('http://10.155.8.166/rbt/v2/utils/nextchargeclass?subscriberId='+number+'&categoryID=3&mode=WAP_HT_APP&clipID=29170281&subType=ringback_musictune') 
#print(request_url.read()) 
response=request_url.read()
#print (jsonList)
loaded_json = json.loads(response)
#print (loaded_json)
status=(loaded_json['subscriber_status'])
print ("Entered number status:",(status))
