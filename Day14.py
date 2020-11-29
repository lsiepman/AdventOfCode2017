# IMPORTS
import re
import numpy as np
from scipy.ndimage import label
from Day10 import part_2 as knot_hash

# DATA
data = "oundnydw"

# GOAL 1
"""
The disk in question consists of a 128x128 grid; 
each square of the grid is either free or used. 
On this disk, the state of the grid is tracked by 
the bits in a sequence of knot hashes.

A total of 128 knot hashes are calculated, 
each corresponding to a single row in the grid; 
each hash contains 128 bits which correspond to individual grid squares. 
Each bit of a hash indicates whether that square is free (0) or used (1).

The hash inputs are a key string (your puzzle input), a dash, 
and a number from 0 to 127 corresponding to the row. 

The output of a knot hash is traditionally represented by 32 hexadecimal digits; 
each of these digits correspond to 4 bits, for a total of 4 * 32 = 128 bits. 
To convert to bits, turn each hexadecimal digit to its equivalent binary value

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
Now, all the defragmenter needs to know is the number of regions. 
A region is a group of used squares that are all adjacent, not including diagonals. 
Every used square is in exactly one region: lone used squares form their own isolated regions, 
while several adjacent squares all count as a single region.

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

