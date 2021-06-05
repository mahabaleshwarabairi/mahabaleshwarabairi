# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:05:58 2020

@author: Mahabaleshwara.Bairi
"""

import urllib.request 
import json
request_url = urllib.request.urlopen('http://10.155.8.166/rbt/v2/subscription/service/voltron?subscriberId=9980900766&storeId=190&mode=WAP_HT_APP') 
#print(request_url.read()) 
response=request_url.read()
#print (jsonList)
loaded_json = json.loads(response)
#print (loaded_json)
#print (loaded_json['allowed_service_list'][0]['charge_class']['service_key'])
data0=(loaded_json['allowed_service_list'][0])
data1=(loaded_json['allowed_service_list'][1])
data2=(loaded_json['allowed_service_list'][2])
data3=(loaded_json['allowed_service_list'][3])
data4=(data0['subscription_class']['service_key'])
data5=(data0['subscription_class']['amount'])
data6=(data1['subscription_class']['service_key'])
data7=(data1['subscription_class']['amount'])
data8=(data2['subscription_class']['service_key'])
data9=(data2['subscription_class']['amount'])
data10=(data3['subscription_class']['service_key'])
data11=(data3['subscription_class']['amount'])
print ("OFFER KEYS ARE")
print (data4+" "+data6+" "+data8+" "+data10+"")
print ("\n")

print ("JSON RESPONSE")
print (loaded_json)
print ("FIRST PART ")
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print (data0)


