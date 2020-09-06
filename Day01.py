# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 21:29:00 2020.

@author: laura
"""


# IMPORTS

# DATA
captcha = []
with (open("Data - Day01.txt")) as file:
    for line in file:
        for char in line.strip():
            captcha.append(char)
# GOAL 1
"""
It goes on to explain that you may only leave by solving a captcha to prove
you're not a human. Apparently, you only get one millisecond to solve the
captcha: too fast for a normal human, but it feels like hours to you.

The captcha requires you to review a sequence of digits (your puzzle input)
and find the sum of all digits that match the next digit in the list.
The list is circular, so the digit after the last digit is the first digit
in the list.

For example:

- 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the
second digit and the third digit (2) matches the fourth digit.
- 1111 produces 4 because each digit (all 1) matches the next.
- 1234 produces 0 because no digit matches the next.
- 91212129 produces 9 because the only digit that matches the next one is the
last digit, 9.

What is the solution to your captcha?"""

# ANSWER 1
captcha.append(captcha[0]) # takes care of the circular list
captcha.append("x") # to end the list

valid_pairs = []
for idx, char in enumerate(captcha):
    if char == "x":
        break
    if captcha[idx] == captcha[idx + 1]:
        valid_pairs.append(int(char))

print(f"The sum equals {sum(valid_pairs)}")
captcha.pop()
captcha.pop() # restore list to original state

# GOAL 2
"""Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:

- 1212 produces 6: the list contains 4 items,
and all four digits match the digit 2 items ahead.
- 1221 produces 0, because every comparison is between a 1 and a 2.
- 123425 produces 4, because both 2s match each other, but no other digit has a match.
- 123123 produces 12.
- 12131415 produces 4.

What is the solution to your new captcha?"""

# ANSWER 2
valid_pairs = []
for idx, char in enumerate(captcha):
    match_idx = int((idx + len(captcha) / 2) % len(captcha))

    if captcha[idx] == captcha[match_idx]:
        valid_pairs.append(int(char))

print(f"The sum equals {sum(valid_pairs)}")

