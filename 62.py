# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:00:52 2020

@author: Mahabaleshwara.Bairi
"""

file1=open ('test1','a')
file1.write('Coke\n')
file1.write('COffie\n')
file1.close()

file1=open ('test1','r')
disp=(file1.read())
print (disp)
