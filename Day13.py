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
 ***REMOVED***

 ***REMOVED***
 ***REMOVED***
 ***REMOVED***

 ***REMOVED***
 ***REMOVED***
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