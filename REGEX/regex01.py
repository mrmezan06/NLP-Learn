# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 23:59:24 2020

@author: Mezan
"""

import re

s = "I was born in 1998"
# 0 or more char
re.match(r".*", s)
# 1 or more char
re.match(r".+", s)
# a-zA-Z char 1 or more than 1 char of a-zA-Z
re.match(r"[a-zA-Z]+","", s)
#ab? means no b or 1b after an a matching
s = "abb"
re.match(r"ab?",s)