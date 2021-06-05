# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:03:53 2020

@author: Mahabaleshwara.Bairi
"""

import re
line="Cats are smarter than dogs" ####match
match=re.match(r'dogs',line,re.M|re.I)
if match:
   print ("match----->",match.group())

else:
    search=re.search(r'dogs',line,re.M|re.I)### search
    if search:
        print ("Search-->",search.group())
    else:
            print ("Nothing found")
            