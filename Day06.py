# DATA
data = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]


# ANSWER 1
def part_1(data):
    states = []

    while data not in states:
        states.append(data[:])
        max_value = max(data)
        idx = data.index(max_value)
        data[idx] = 0
        while max_value:
            idx = (idx + 1) % len(data)
            data[idx] += 1
            max_value -= 1

    print(f"Answer 6a: {len(states)}")


part_1(data.copy())

# GOAL 2
"""
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
            idx = (idx + 1) % len(data)
            data[idx] += 1
            max_value -= 1

    print(f"Answer 6b: {len(states) - states.index(data)}")


part_2(data.copy())
