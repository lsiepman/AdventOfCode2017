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
"""Each instruction consists of several parts: the register to modify, 
whether to increase or decrease that register's value, the amount by which to increase or decrease it, 
and a condition. If the condition fails, skip the instruction without modifying the register.
The registers all start at 0. 

You might also encounter <= (less than or equal to) or != (not equal to). 
However, the CPU doesn't have the bandwidth to tell you what all the registers are named, 
and leaves that to you to determine.

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
"""To be safe, the CPU also needs to know the highest value held in any register during 
this process so that it can decide how much memory to allocate to these operations. 
For example, in the above instructions, the highest value ever held was 10 
(in register c after the third instruction was evaluated)."""

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