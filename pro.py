# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:10:07 2020

@author: mahabaleshwara.bairi
"""
import subprocess
#Command 1 def uname_func():
uname = "uname"
uname_arg = "-a"
print ("Gathering system information with %s command:\n" % uname)
subprocess.call([uname, uname_arg])
