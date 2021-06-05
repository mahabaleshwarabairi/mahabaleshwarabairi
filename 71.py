# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:32:06 2020

@author: Mahabaleshwara.Bairi
"""

#!/usr/bin/python

def file_readline_test(file_name):
	file_open = open(file_name, "rb")
	print ("File name is : %s" %(file_open.name))
	fl_rdline = file_open.readline()
	print ("File read line value is : %s" %(fl_rdline))
	fl_rdline = file_open.readline(5)
	print ("File read line value for 5 is : %s" %(fl_rdline))
	if (file_open.closed):
		print ("File already closed")
	else:
		file_open.close()

if ( __name__ == "__main__" ):
	file_readline_test("test_file.txt")
else:
	print ("Method name is not main")
