# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 22:06:15 2020.

@author: laura
"""

# IMPORTS

# DATA
spreadsheet = []
with open("Data - Day02.txt") as file:
    for line in file:
        row = line.split("\t")
        spreadsheet.append([int(i) for i in row])


# GOAL 1
"""What is the checksum for the spreadsheet in your puzzle input?"""


# ANSWER 1
def calc_checksum(data):
    checksum = 0
    for sublist in data:
        checksum += max(sublist) - min(sublist)

    return checksum


checksum = calc_checksum(spreadsheet)
print(f"Answer 2a: {checksum}")

# GOAL 2
""""What is the sum of each row's result in your puzzle input?"""


def calc_divisible_rowsum(data):
    rowsum = 0

    for sublist in data:
        len_sublist = len(sublist)
        for val in sublist:
            for idx in range(len_sublist):
                if val != sublist[idx] and val % sublist[idx] == 0:
                    rowsum += val / sublist[idx]

    return rowsum


rowsum = calc_divisible_rowsum(spreadsheet)
print(f"Answer 2b: {int(rowsum)}")
