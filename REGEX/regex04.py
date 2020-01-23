# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 00:51:15 2020

@author: Mezan
"""

import re

s1 = "Welcome to the year 2020"
s2 = "Just ~% +++----arrived at @Jack's place. #fun"
s3 = "I               love              you"

s1_modified = re.sub(r"\d","",s1)
# \. escaping the meaning of all character of dot(.)
s2_modified = re.sub(r"[@#%~+-\.']","",s2)
# w - word character --> remove all word symbol from string group of class --> [a-zA-Z0-9]
s2_modified = re.sub(r"\w","",s2)
# W - ASCII Character or not Word Character
s2_modified = re.sub(r"\W"," ",s2)
#replace all the space with one space
s2_modified = re.sub(r"\s+"," ",s2_modified)

# removing single character of which no meaning
s2_modified = re.sub(r"\s+[a-zA-Z]\s+"," ",s2_modified)
# replace extra space from sentence
s3_modified = re.sub(r"\s+love\s+"," hate ",s3)