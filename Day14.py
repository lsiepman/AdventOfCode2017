# IMPORTS
import re
import numpy as np
from scipy.ndimage import label
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
    for i in range(max_val):
        output.append(knot_hash(f"{data}-{i}"))

    return output

def hex_to_bin(hash):
    bin_values = []
    for i in hash:
        val = re.search("[01]+$", bin(int(i, 16))).group()
        
        if len(val) == 1:
            val = "000" + val
        elif len(val) == 2:
            val = "00" + val
        elif len(val) == 3:
            val = "0" + val
        
        bin_values.append(val)

    return "".join(bin_values)

def count_used(bin_values):
    total = 0
    for val in bin_values:
        for i in val:
            if i == "1":
                total += 1
    return total

def solve_1(data):
    hash_vals = hashes(data, 128)
    bin_vals = []
    for h in hash_vals:
        bin_vals.append(hex_to_bin(h))

    print(f"{count_used(bin_vals)} squares have been used")
    return bin_vals

bins = solve_1(data)

# GOAL 2
"""
***REMOVED***
A region is a group of used squares that are all adjacent, not including ***REMOVED*** 
***REMOVED***
***REMOVED***

How many regions are present given your key string?
"""
def create_grid(inp):
    grid = np.zeros((128, 128))
    for i,j in enumerate(inp):
        grid[i] = np.array(list(j))

    return grid.astype(int)
    

def solve_2(bins):
    grid = create_grid(bins)
    print(f"Answer part2: {label(grid)[1]}")

solve_2(bins)

