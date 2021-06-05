# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:19:38 2020

@author: Mahabaleshwara.Bairi
"""

#!/usr/bin/python

def file_read(file_name):
    file_open=('file_name',"rb")
    print ("File Name is %s:"%(file_open.name  ))
    file1=file_open.readline()
    print ("File read line value is %s"%(file1))
    file2=file_open.readline(5)
    print ("File readline values is %s"%(file2))
    file_open.close()
    
    file_read('8.py')
    
    