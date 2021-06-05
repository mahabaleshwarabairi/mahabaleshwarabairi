# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:36:05 2020

@author: Mahabaleshwara.Bairi
"""

#!/usr/bin/python

def file_readlines_test(file_name):
	file_open = open(file_name, "r")
	print ("File name is : %s" %(file_open.name))
	fl_rdlines = file_open.readlines.strip()
	print ("File contents are : %s" %(fl_rdlines))
	fl_rdlines = file_open.readlines(5)
	print ("File contents for 5 value is : %s" %(fl_rdlines))
	if (file_open.closed):
		print ("File already closed")
	else:
		file_open.close()

if ( __name__ == "__main__" ):
	file_readlines_test("test_file.txt")
else:
	print ("Method name is not main")

