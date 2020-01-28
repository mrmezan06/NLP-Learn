# -*- coding: utf-8 -*-

import nltk as nk

p = "The Taj Mohal was built by Emperor Shah Jahan"
#p = "Highest Guinness Record holder in Bangladesh"
#p = "The Official Website of Taylor Swift - Lover Album Out Now! Festival & Concert Details, Ticket Information, Videos, Merchandise & More."
w = nk.word_tokenize(p)

t_w = nk.pos_tag(w)
n_entity = nk.ne_chunk(t_w)

n_entity.draw()


"""
ORGANIZATION	Georgia-Pacific Corp., WHO
PERSON	Eddy Bonte, President Obama
LOCATION	Murray River, Mount Everest
DATE	June, 2008-06-29
TIME	two fifty a m, 1:30 p.m.
MONEY	175 million Canadian Dollars, GBP 10.40
PERCENT	twenty pct, 18.75 %
FACILITY	Washington Monument, Stonehenge
GPE	South East Asia, Midlothian
"""