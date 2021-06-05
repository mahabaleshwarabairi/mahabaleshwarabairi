# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 23:07:05 2020

@author: Mahabaleshwara.Bairi
"""

#!/usr/bin/python

def function_change_value_test(list1):
	print ("List 1 value is : %s" %(list1))
	list1.append(['5, 8, 9, 10, 4, 28'])
	print ("List 1 values after appending values are : %s" %(list1))
	return

if ( __name__ == "__main__" ):
	list1 = [4, 8, 12, 8, 32, 7, 9]
	function_change_value_test(list1)
	print ("List 1 values after appending new values in function is : %s" %(list1))
else:
	print ("Method name is not main")

