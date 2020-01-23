# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 00:38:58 2020

@author: Mezan
"""

import re

sen = "I Love AAA"
# Substitute AAA as string or [A]+ same three A matching but [A] return 3 times ANIKA
print(re.sub(r"AAA","AKASH",sen))
# case sensitive
print(re.sub(r"[a-z]","1",sen))
# case sensitive disable
print(re.sub(r"[a-z]","1",sen,flags=re.I))
# Count to replace
print(re.sub(r"[a-z]","1",sen,5,flags=re.I))