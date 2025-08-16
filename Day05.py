# IMPORTS

# DATA
data = []
with open("Data - Day05.txt") as file:
    for line in file:
        data.append(int(line))

part2_data = data.copy()


# ANSWER 1
def part_1(data):
    final = len(data)

    count = 0
    idx = 0
    while idx < final:
        val = data[idx]
        data[idx] += 1
        idx = idx + val
        count += 1

    print(f"Answer 5a: {count}")


part_1(data)


# ANSWER 2
def part_2(data):
    final = len(data)

    count = 0
    idx = 0
    while idx < final:
        val = data[idx]
        if val >= 3:
            data[idx] -= 1
        else:
            data[idx] += 1

        idx = idx + val
        count += 1

    print(f"Answer 5b: {count}")


part_2(part2_data)
