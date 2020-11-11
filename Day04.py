# IMPORTS

# DATA
data = []
with open("Data - Day04.txt") as file:
    for line in file:
        data.append(line.strip().split(" "))

# GOAL 1
"""
A new system policy has been put in place that requires all accounts to use a passphrase 
instead of simply a password. 
A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?
"""

# ANSWER 1
data_sets = []
for phrase in data:
    data_sets.append(set(phrase))

num_valid = 0
for i in range(len(data)):
    if len(data[i]) == len(data_sets[i]):
        num_valid += 1

print(f"Answer 4a: {num_valid}")

# GOAL 2
"""
For added security, yet another system policy has been put in place. 
Now, a valid passphrase must contain no two words that are anagrams of each other - that is, 
a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.
"""

def is_anagram(phrase):
    alpha_phrase = []
    for word in phrase:
        alpha_word = sorted(word)
        alpha_phrase.append("".join(alpha_word))

    return alpha_phrase

sorted_data = []
sorted_data_sets = []
for i in data:
    new_i = is_anagram(i)
    sorted_data.append(new_i)
    sorted_data_sets.append(set(new_i))


num_valid_b = 0
for i in range(len(sorted_data)):
    if len(sorted_data[i]) == len(sorted_data_sets[i]):
        num_valid_b += 1

print(f"Answer 4b: {num_valid_b}")