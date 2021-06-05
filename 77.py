# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 23:04:55 2020

@author: Mahabaleshwara.Bairi
"""

#!/usr/bin/python

def function_change_value_override_test(list1):
	print ("List 1 values are : %s" %(list1))
	list1 = [45, 23, 63, 35, 99, 74]
	print ("List 1 values after assigning new values is : %s" %(list1))
	return

if ( __name__ == "__main__" ):
	list1 = [2, 8, 7, 34, 0, 7, 23, 7, 80, 3]
	function_change_value_override_test(list1)
	print ("List 1 values outside the function is : %s" %(list1))
else:
	print ("Method name is not main")
