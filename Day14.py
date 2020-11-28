# IMPORTS
from Day10 import part_2 as knot_hash

# DATA
data = "oundnydw"

# GOAL 1
"""
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***

***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***

***REMOVED***
***REMOVED***

***REMOVED***
***REMOVED***
***REMOVED***

Given your actual key string, how many squares are used?
"""

def hashes(data, max_val):
    output = []
    for i in range(128):
        output.append(knot_hash(f"{data}-{i}"))

    return output


hash_vals = hashes(data, 128)
