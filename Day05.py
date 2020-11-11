# IMPORTS

# DATA
data = []
with open("Data - Day05.txt") as file:
    for line in file:
        data.append(int(line))

part2_data = data.copy()
# GOAL 1
"""
An urgent interrupt arrives from the CPU: 
it's trapped in a maze of jump instructions, 
and it would like assistance from any programs with spare cycles to help find the exit.

The message includes a list of the offsets for each jump. 
Jumps are relative: -1 moves to the previous instruction, 
and 2 skips the next one. 
Start at the first instruction in the list. 
The goal is to follow the jumps until one leads outside the list.

In addition, these instructions are a little strange; after each jump, 
the offset of that instruction increases by 1. So, if you come across an offset of 3, 
you would move three instructions forward, but change it to a 4 for the next time it is encountered.
"""

# ANSWER 1
def part_1(data):
    final = len(data)
    
    count = 0
    idx = 0
    while idx < final:
        val = data[idx]
        data[idx] += 1
        idx = idx + val
        count += 1
    
    print(f"Answer 5a: {count}")

part_1(data)

# GOAL 2
"""
Now, the jumps are even stranger: after each jump, 
if the offset was three or more, instead decrease it by 1. 
Otherwise, increase it by 1 as before.

How many steps does it now take to reach the exit?
"""

# ANSWER 2
def part_2(data):
    final = len(data)
    
    count = 0
    idx = 0
    while idx < final:
        val = data[idx]
        if val >= 3:
            data[idx] -= 1
        else:
            data[idx] += 1
        
        idx = idx + val
        count += 1
    
    print(f"Answer 5b: {count}")

part_2(part2_data)
