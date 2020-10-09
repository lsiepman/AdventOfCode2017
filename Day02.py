# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 22:06:15 2020.

@author: laura
"""

# IMPORTS

# DATA
spreadsheet = []
with(open("Data - Day02.txt")) as file:
    for line in file:
        row = line.split("\t")
        spreadsheet.append([int(i) for i in row])


# GOAL 1
"""
The spreadsheet consists of rows of apparently-random numbers.
To make sure the recovery process is on the right track,
they need you to calculate the spreadsheet's checksum.
For each row, determine the difference between the largest value and the
smallest value; the checksum is the sum of all of these differences.

What is the checksum for the spreadsheet in your puzzle input?"""

# ANSWER 1
def calc_checksum(data):
    checksum = 0
    for sublist in data:
        checksum += (max(sublist) - min(sublist))

    return checksum

checksum = calc_checksum(spreadsheet)
print(f"Answer 2a: {checksum}")

# GOAL 2
""""Based on what we're seeing, it looks like all the User wanted is some
information about the evenly divisible values in the spreadsheet.
Unfortunately, none of us are equipped for that kind of calculation -
most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where
one evenly divides the other - that is, where the result of the division
operation is a whole number. They would like you to find those numbers on
each line, divide them, and add up each line's result.

What is the sum of each row's result in your puzzle input?
"""
def calc_divisible_rowsum(data):
    rowsum = 0

    for sublist in data:
        len_sublist = len(sublist)
        for val in sublist:
            for idx in range(len_sublist):
                if val != sublist[idx] and val % sublist[idx] == 0:
                    rowsum += (val / sublist[idx])

    return rowsum

rowsum = calc_divisible_rowsum(spreadsheet)
print(f"Answer 2b: {int(rowsum)}")
