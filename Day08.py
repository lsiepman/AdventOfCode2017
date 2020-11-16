# IMPORTS
import pandas as pd

# DATA
data = []
with open("Data - Day08.txt") as file:
    for line in file:
        data.append(line.strip().split(" "))
data = pd.DataFrame(data, columns=["register", "action", "action_value", "if_col", "condition_register", "condition", "condition_value"])
data["action_value"] = pd.to_numeric(data["action_value"])
data["condition_value"] = pd.to_numeric(data["condition_value"])
# GOAL 1
"""***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***

***REMOVED***
***REMOVED***
***REMOVED***

What is the largest value in any register after completing the instructions in your puzzle input? 
"""

# ANSWER 1
registers = list(data["register"]) + list(data["condition_register"])
registers = list(set(registers))
reg_dict = {}
for i in registers:
    reg_dict[i] = 0

def inc(reg_dict, register, value):
    reg_dict[register] += value

def dec(reg_dict, register, value):
    reg_dict[register] -= value

def check_condition(reg_dict, condition_register, condition, condition_value):
    cond = reg_dict[condition_register]
        
    if condition == "<":
        if cond < condition_value:
            return True
    elif condition == ">":
        if cond > condition_value:
            return True
    elif condition == "<=":
        if cond <= condition_value:
            return True
    elif condition == ">=":
        if cond >= condition_value:
            return True
    elif condition == "==":
        if cond == condition_value:
            return True
    elif condition == "!=":
        if cond != condition_value:
            return True 
    
    return False

def part_1(data, reg_dict):
    idx = 0
    while idx < 1000:
        status = check_condition(reg_dict, data["condition_register"][idx], data["condition"][idx], data["condition_value"][idx])
        if status is True:
            if data["action"][idx] == "inc":
                inc(reg_dict, data["register"][idx], data["action_value"][idx])
            elif data["action"][idx] == "dec":
                dec(reg_dict, data["register"][idx], data["action_value"][idx])

        idx += 1
    
    return reg_dict

final_state_registers = part_1(data, reg_dict)
print(f"Answer 8a: {max(final_state_registers.values())}")

# GOAL 2
"""***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***"""

reg_dict = {}
for i in registers:
    reg_dict[i] = 0
    
def part_2(data, reg_dict):
    idx = 0
    max_value = 0
    while idx < 1000:
        status = check_condition(reg_dict, data["condition_register"][idx], data["condition"][idx], data["condition_value"][idx])
        if status is True:
            if data["action"][idx] == "inc":
                inc(reg_dict, data["register"][idx], data["action_value"][idx])
            elif data["action"][idx] == "dec":
                dec(reg_dict, data["register"][idx], data["action_value"][idx])
        
        max_now = max(reg_dict.values())
        if max_now > max_value:
            max_value = max_now

        idx += 1
    
    return max_value

print(f"Answer 8b: {part_2(data, reg_dict)}")