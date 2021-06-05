# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:34:52 2020

@author: Mahabaleshwara.Bairi
"""

class P:
    def __init__(self,name): #####special method [const]
        self.guy=name
    def ask(self):
        print ("Hello , My name is ",self.guy)
p=P('MAHA BAIRI')
p.ask()
