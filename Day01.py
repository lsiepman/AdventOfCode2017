# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 21:29:00 2020.

@author: laura
"""


# IMPORTS

# DATA
captcha = []
with open("Data - Day01.txt") as file:
    for line in file:
        for char in line.strip():
            captcha.append(char)
# GOAL 1
"""What is the solution to your captcha?"""

# ANSWER 1
captcha.append(captcha[0])  # takes care of the circular list
captcha.append("x")  # to end the list

valid_pairs = []
for idx, char in enumerate(captcha):
    if char == "x":
        break
    if captcha[idx] == captcha[idx + 1]:
        valid_pairs.append(int(char))

print(f"The sum equals {sum(valid_pairs)}")
captcha.pop()
captcha.pop()  # restore list to original state

# GOAL 2
"""What is the solution to your new captcha?"""

# ANSWER 2
valid_pairs = []
for idx, char in enumerate(captcha):
    match_idx = int((idx + len(captcha) / 2) % len(captcha))

    if captcha[idx] == captcha[match_idx]:
        valid_pairs.append(int(char))

print(f"The sum equals {sum(valid_pairs)}")
