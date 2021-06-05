# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:16:35 2020

@author: Mahabaleshwara.Bairi
"""

#re.M multiple line
#re.I 
import re
line="Cats are smarter than dogs"
matchobj=re.match(r'(.*) are (.*) (.*)', line ,re.M|re.I)#####match syntax 
if matchobj:
    print ("matchobj,group():",matchobj.group())
    print ("matchobj,group(1):",matchobj.group(1))
    print ("matchobj,group(2):",matchobj.group(2))
    print ("matchobj,group(3):",matchobj.group(3))
   
   