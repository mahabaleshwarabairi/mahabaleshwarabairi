# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 23:09:56 2020

@author: Mahabaleshwara.Bairi
"""

#!/usr/bin/python

def function_default_keyword_test(str1, str2 = "Test 2"):
	print ("Str 1 value is : %s" %(str1))
	print ("Str 2 value is : %s \n" %(str2))
	return

if ( __name__ == "__main__" ):
	function_default_keyword_test(str1 = "Test1", str2 = "Test4")
	function_default_keyword_test(str1 = "Test2")
else:
	print ("Method name is not main")
