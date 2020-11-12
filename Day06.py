# DATA
data = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
# GOAL 1
"""
A debugger program here is having an issue: 
it is trying to repair a memory reallocation routine, 
but it keeps getting stuck in an infinite loop.

In this area, there are sixteen memory banks; 
each memory bank can hold any number of blocks. 
The goal of the reallocation routine is to balance the blocks between the memory banks.

The reallocation routine operates in cycles. In each cycle, it finds the memory bank with the most blocks 
(ties won by the lowest-numbered memory bank) and redistributes those blocks among the banks. To do this, 
it removes all of the blocks from the selected bank, then moves to the next (by index) memory bank and 
inserts one of the blocks. It continues doing this until it runs out of blocks; if it reaches the last memory bank,
it wraps around to the first one.

The debugger would like to know how many redistributions can be done before a blocks-in-banks configuration is 
produced that has been seen before. Given the initial block counts in your puzzle input, 
how many redistribution cycles must be completed before a configuration is produced that has been seen before?
"""
# ANSWER 1
def part_1(data):
    states = []

    while data not in states:
        states.append(data[:])
        max_value = max(data)
        idx = data.index(max_value)
        data[idx] = 0
        while max_value:
            idx = (idx + 1)% len(data)
            data[idx] += 1
            max_value -= 1

    print(f"Answer 6a: {len(states)}")

part_1(data.copy())

# GOAL 2
"""Out of curiosity, the debugger would also like to know the size of the loop: 
starting from a state that has already been seen, how many block redistribution 
cycles must be performed before that same state is seen again?

How many cycles are in the infinite loop that arises from the configuration in your puzzle input?
"""

def part_2(data):
    states = []

    while data not in states:
        states.append(data[:])
        max_value = max(data)
        idx = data.index(max_value)
        data[idx] = 0
        while max_value:
            idx = (idx + 1)% len(data)
            data[idx] += 1
            max_value -= 1

    print(f"Answer 6b: {len(states) - states.index(data)}")

part_2(data.copy())