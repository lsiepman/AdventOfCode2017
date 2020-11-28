# IMPORTS
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
    for i in range(128):
        output.append(knot_hash(f"{data}-{i}"))

    return output


hash_vals = hashes(data, 128)
