# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:16:34 2020

@author: Mahabaleshwara.Bairi
"""

#!/usr/bin/python

def file_read_test():
	file_open = open("filewrite.py", "rb")
	fl_rd = file_open.read()
	print "Data read from file %s is :" %(file_open.name)
	print "%s" %(fl_rd)
	if (file_open.closed):
		print "File already closed"
	else:
		file_open.close()

	file_read_test()
