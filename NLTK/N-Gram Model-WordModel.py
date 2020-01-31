# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 06:17:35 2020

@author: Mezan
"""

import random
import nltk

# Sample data
text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

# n is bigger and accuracy is also bigger
n = 3

ngrms = {}

# tokenization with nltk
words = nltk.word_tokenize(text)

for i in range(len(words)-n):
    gram = ' '.join(words[i:i+n])
    if gram not in ngrms.keys():
        ngrms[gram] = []
    ngrms[gram].append(words[i+n])

# Testing The Model
cGram = ' '.join(words[0:n])
result = cGram
# 30 word string
for i in range(30):
    if cGram not in ngrms.keys():
        break
    possibilitied = ngrms[cGram]
    nxtItem = possibilitied[random.randrange(len(possibilitied))]
    result += ' '+nxtItem
    rwords = nltk.word_tokenize(result)
    cGram = ' '.join(rwords[len(rwords)-n:len(rwords)])
    
print(result)