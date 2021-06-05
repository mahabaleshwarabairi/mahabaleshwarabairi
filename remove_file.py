# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:07:29 2020

@author: mahabaleshwara.bairi
"""

from datetime import date
from pathlib import path
import os
for x in path('C:/\Users/\mahabaleshwara.bairi').glob('*.txt'):
    if (date.today())-date.fromtimestamp(x.stat().st_mtime).days>7:
        print('removed:',x)
        x.unlink()
        