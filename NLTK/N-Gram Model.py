# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 05:49:45 2020

@author: Mezan
"""

import random

# Sample data
text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

# Character N-Gram Model
# It is trigram that's why n = 3
# Increasing number of n is give better result
n = 6

ngrams = {}

# Create the n-grams
for i in range(len(text)-n):
    gram = text[i:i+n] #text[0:3] = Glo
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(text[i+n])

# Testing N-Gram model
cGram = text[0:n] #Start Point
result = cGram
# 100 len word
for i in range(100):
    if cGram not in ngrams.keys():
        break
    possibilities = ngrams[cGram]
    nxtItem = possibilities[random.randrange(len(possibilities))]
    result += nxtItem
    cGram = result[len(result)-n:len(result)]
    
print(result)