# IMPORTS
import re

# DATA
file = open("Data - Day09.txt")
data = file.read().strip()
# GOAL 1
"""The characters represent groups - sequences that begin with { and end with }. 
Within a group, there are zero or more other things, separated by commas: 
either another group or garbage. Groups are nestable. 
Your puzzle input represents a single, large group which itself contains many smaller ones.

Sometimes, instead of a group, you will find garbage. 
Garbage begins with < and ends with >. Between those angle brackets, almost any character can appear, 
including { and }. Within garbage, < has no special meaning.

In a futile attempt to clean up the garbage, 
some program has canceled some of the characters within it using !
inside garbage, any character that comes after ! should be ignored, including <, >, and even another !.

You don't see any characters that deviate from these rules. Outside garbage, you only find well-formed groups, 
and garbage always terminates according to the rules above.

Your goal is to find the total score for all groups in your input. 
Each group is assigned a score which is one more than the score of the 
group that immediately contains it. (The outermost group gets a score of 1.)
"""

# ANSWER 1
without_cancel = re.sub(r"!.{1}", "", data)
without_garbage = re.sub(r"<[^>]*>", "", without_cancel)

def get_score(text):
    score = 0

    current_level = 0
    for i in text:
        if i == "{":
            current_level += 1
        elif i == "}":
            score += current_level 
            current_level -= 1
        else:
            pass
    
    return score

print(f"Answer 9a: {get_score(without_garbage)}")

# GOAL 2
"""
To prove you've removed it, you need to count all of the characters within the garbage. 
The leading and trailing < and > don't count, nor do any canceled characters or the ! doing the canceling.

How many non-canceled characters are within the garbage in your puzzle input?
"""

garbage = re.findall(r"<([^>]*)>", without_cancel)
garbage_text = "".join(garbage)

print(f"Answer 9b: {len(garbage_text)}")