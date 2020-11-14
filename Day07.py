# IMPORTS
import re
from collections import Counter

# DATA
data = []
with open("Data - Day07.txt") as file:
    for line in file:
        data.append(line.strip())

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

What is the name of the bottom program?
"""
# ANSWER 1 Which disc isn't carried by an other disc
carriers = []
carried = []
for i in data:
    carriers.append(re.search("^[a-z]+", i).group())
    after_arrow = re.search("->.*$", i)
    if after_arrow is not None:
        carried.extend(re.findall("[a-z]+", after_arrow.group()))

for i in carriers:
    if i not in carried:
        print(f"Answer 7a: {i}")

# GOAL 2
"""
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***

Given that exactly one program is the wrong weight, what would its weight need to be to balance the entire tower?
"""

# ANSWER 2
# create dict with all weights
weights = {}
for i in data:
    disc = re.search("^[a-z]+", i).group()
    weights[disc] = int(re.search(f"{disc} \(([0-9]+)\)", i).group(1))

stack = {}
for i in data:
    bottom = re.search("^[a-z]+", i).group()
    after_arrow = re.search("->.*$", i)
    if after_arrow is not None:
        top = re.findall("[a-z]+", after_arrow.group())
    else:
        top = []
    
    stack[bottom] = top
    
def find_all_stacked(stack, key):
    stacked = [key]
    if key in stack.keys() and len(stack[key]) > 0:
        for i in stack[key]:
            stacked.extend(find_all_stacked(stack, i))
    
    return stacked
        
total_weights = {}
for i in list(stack.keys()):
    discs = find_all_stacked(stack, i)
    sum_weight = 0
    for w in discs:
        sum_weight += weights[w]
    
    total_weights[i] = sum_weight

def find_values_stack(total_weights, stack, key):
    temp_values = []
    temp_keys = []

    if not isinstance(stack[key], list):
        print("Non-carrying key:", key)
        return key, total_weights[key]

    for i in stack[key]:
        temp_values.append(total_weights[i])
        temp_keys.append(i)

    return temp_values, temp_keys

def check_balance(total_weights, stack, key):
    temp_values, temp_keys = find_values_stack(total_weights, stack, key)

    if len(set(temp_values)) == 1:
        print("Equal weights, key has an offset", key)
        return key, total_weights[key]

    cnt = Counter(temp_values).most_common()[-1][0]
    idx = temp_values.index(cnt)

    return temp_keys[idx]

status = True
key = "mkxke"
all_keys = []
while status:
    key = check_balance(total_weights, stack, key)
    if isinstance(key, tuple):
        status = False
    else:
        all_keys.append(key)

key_before_offset = all_keys[-2]
desired_values, keys = find_values_stack(total_weights, stack, key_before_offset)
idx_offset = keys.index(all_keys[-1])
offset = desired_values[idx_offset + 1 % len(desired_values)] - desired_values[idx_offset]

print(f"Program {all_keys[-1]} would need to be {weights[all_keys[-1]] + offset} instead of {weights[all_keys[-1]]}")