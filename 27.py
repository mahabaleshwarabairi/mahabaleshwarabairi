# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:13:22 2020

@author: Mahabaleshwara.Bairi
"""
states={
        'TN' : {'capital':'Chenai','language':'Tamil'}, 
        'KL': {'capital':'trivandarm','language':'Keralla'},
        'KK':{'capital':'BNG','language':'KAN'}
    }

labels ={'capital':'capital city',
        'language':'spoken language'}
state=input("Please enter state:")
fetch=input("capital (C) or L..?")
if fetch=='C': key='capital'
if fetch=='L':key='language'
if  state in states:
    print("%s 's %s is %s" %(state,labels[key],states[state][key]))
    