# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:47:03 2020

@author: Mahabaleshwara.Bairi
"""

import re
regex=r"([a-zA-Z]+) (\d+)"
if re.search(regex,"April 18"):
    match =re.search(regex,"April 18")
    print ("Match at index %s , %s" %(match.start(),match.end()))
    print ("Full Match : %s" %(match.group(0)))
    print ("Month :%s" %(match.group(1)))
    print ("Day :%s"%(match.group(2)))
else:
    print ("The regex patterns does not match:(")
    