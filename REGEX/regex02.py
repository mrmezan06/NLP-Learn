# -*- coding: utf-8 -*-

import re

#sen = "I was born in the year 1998"
sen = "1998 was my borning year"
# no match because of only the first pattern it is match whenever it didn't find any match so return nothing
re.match(r"[a-zA-Z]+", sen)
# it is matching whole sentence and return first match it was got
re.search(r"[a-zA-Z]+", sen)

# Starts with
if re.match(r"^1998", sen):
    print("Matched!")
else:
    print("No Match!")
    
# Ends with direct sentence year$, [a-zA-Z]*$, [a-zA-Z]+$ all of them can matched
if re.search(r"year$", sen):
    print("Matched!")
else:
    print("No Match!")