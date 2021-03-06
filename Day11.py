# IMPORTS

# DATA
data = []
with open("Data - Day11.txt") as file:
    for line in file:
        for direction in line.strip().split(","):
            data.append(direction)

# GOAL 1
"""
The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north,
 northeast, southeast, south, southwest, and northwest:

You have the path the child process took. 
Starting where he started, you need to determine the
fewest number of steps required to reach him. 
(A "step" means to move from the hex you are in to any adjacent hex.)
"""
# ANSWER 1
def find_kid(data):
    y = 0 # North - South 
    x = 0 # North West - South East
        
    for direction in data:
        if direction == "n":
            y += 1
        elif direction == "s":
            y -= 1
        elif direction == "nw":
            x += 1
        elif direction == "se":
            x -= 1
        elif direction == "ne":
            x -= 1
            y += 1
        elif direction == "sw":
            x += 1
            y -= 1
    
    return abs(y), abs(x), abs(-x-y)

location = find_kid(data)
print(f"Distance to kid: {sum(location) / 2} tiles")

# Goal 2
"""
How many steps away is the furthest he ever got from his starting position?
"""
def max_dist(data):
    y = 0 # North - South 
    x = 0 # North West - South East
    max_loc = 0
    
    for direction in data:
        if direction == "n":
            y += 1
        elif direction == "s":
            y -= 1
        elif direction == "nw":
            x += 1
        elif direction == "se":
            x -= 1
        elif direction == "ne":
            x -= 1
            y += 1
        elif direction == "sw":
            x += 1
            y -= 1
        max_loc = max(abs(y), abs(x), abs(-x-y), max_loc)

    return max_loc

print(f"Max distance kid: {max_dist(data)}")