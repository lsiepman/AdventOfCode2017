# IMPORTS
import re

# DATA
data = []
with open("Data - Day13.txt") as file:
    for line in file:
        depth = int(re.search(r"^[0-9]+", line).group())
        rnge = int(re.search(r"[0-9]+$", line).group())
        data.append((depth, rnge))
# GOAL 1
"""
By studying the firewall briefly, you are able to record 
(in your puzzle input) the depth of each layer and the range
 of the scanning area for the scanner within it, written as 
 depth: range. Each layer has a thickness of exactly 1. 
 A layer at depth 0 begins immediately inside the firewall; 
 a layer at depth 1 would start immediately after that.

 Your plan is to hitch a ride on a packet about to move through the firewall. 
 The packet will travel along the top of each layer, and it moves at one layer per picosecond. 
 Each picosecond, the packet moves one layer forward (its first move takes it into layer 0), 
 and then the scanners move one step. 
 If there is a scanner at the top of the layer as your packet enters it, 
 you are caught. 
 (If a scanner moves into the top of its layer while you are there, 
 you are not caught: it doesn't have time to notice you before you leave.)

 The severity of getting caught on a layer is equal to its depth multiplied by its range. 
 (Ignore layers in which you do not get caught.) 
 The severity of the whole trip is the sum of these values.

 Given the details of the firewall you've recorded, 
 if you leave immediately, what is the severity of your whole trip?
"""
# ANSWER 1
def part_1(data):
    total = 0
    for depth, rnge in data:
            if depth % (2*rnge - 2) == 0:
                total += depth * rnge       
    
    print(f"Total severity = {total}")

part_1(data)

# GOAL 2
"""
What is the fewest number of picoseconds that you need to 
delay the packet to pass through the firewall without being caught?
"""

# ANSWER 2
def part_2(data, min_val, max_val):
    for delay in range(min_val, max_val):
        total = 0
        for depth, rnge in data:
                if (depth + delay) % (2*rnge - 2) == 0:
                    total += (depth + delay) * rnge 

        if total == 0:
            return delay
            
    
print(f"Delay needed = {part_2(data, 0, 10000000)}")