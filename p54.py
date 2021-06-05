# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:51:41 2020

@author: Mahabaleshwara.Bairi
"""

import re
t="A fat cat doesn\'t eat oat but a rat eats bats."
mo=re.findall("[force]at",t)
print (mo)