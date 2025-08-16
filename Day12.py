# IMPORTS
import re

# DATA
data = {}
with open("Data - Day12.txt") as file:
    for line in file:
        key = re.search("^[0-9]+", line).group()
        connections = re.search(r">([0-9,\s]+)", line).group(1).strip()
        data[key] = connections.split(", ")

# GOAL 1
"""
How many programs are in the group that contains program ID 0?
"""


# ANSWER 1
def find_connections(data, group="0"):
    old = set(group)
    new = set()

    while True:
        for i in old:
            new.update(data[i])

        if len(old) == len(new):
            return len(new)
        else:
            old.update(new)


print(f"Answer part 1: {find_connections(data)}")

# GOAL 2
"""
Now, they would like you to determine the total number of groups.
"""


def find_members(data, group):
    old = set([group])
    new = set()

    while True:
        old_length = len(old)
        for i in old:
            new.update(data[i])

        old = old | new
        if len(old) == old_length:
            return old


def find_groups(data):
    all_progs = set(data.keys())
    grouped_progs = set()
    num_groups = 0

    while len(grouped_progs) < len(all_progs):
        not_in_common = all_progs - grouped_progs
        progs = find_members(data, group=list(not_in_common)[0])
        grouped_progs.update(progs)
        num_groups += 1

    return num_groups


print(f"There are {find_groups(data)} groups in the data")
