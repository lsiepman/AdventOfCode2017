# IMPORTS

# DATA
data = []
with open("Data - Day11.txt") as file:
    for line in file:
        for direction in line.strip().split(","):
            data.append(direction)

# GOAL 1
"""
***REMOVED***
 ***REMOVED***

***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
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