# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:39:57 2020

@author: Mahabaleshwara.Bairi
"""

import re
place ='{city}'
visit='I visted {city} last week'
result=re.sub(place,'jaipur',visit)
print (result)