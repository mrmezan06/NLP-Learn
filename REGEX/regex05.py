# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 01:22:40 2020

@author: Mezan
"""
import re
X = ["This is a wolf @scary",
     "Welcome to the jungle #missing",
     "111322 the number to know",
     "Remember the name s - John",
     "I                love               you"]

for i in range(len(X)):
    X[i] = re.sub(r"\W"," ",X[i])
    print(X[i])
    X[i] = re.sub(r"\d"," ",X[i])
    print(X[i])
    X[i] = re.sub(r"\s+[a-zA-Z]\s+"," ",X[i])
    print(X[i])
    X[i] = re.sub(r"\s+"," ",X[i])
    print(X[i])
    X[i] = re.sub(r"^\s","",X[i])
    X[i] = re.sub(r"\s$","",X[i])
    print(X[i])