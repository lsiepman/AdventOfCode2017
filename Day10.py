# IMPORTS
from operator import xor
from functools import reduce

# DATA
numbers = list(range(256))
data = []


def part_1(numbers, data):
    skip_size = 0
    position = 0

    for i in data:
        # check if length is greater than numbers list
        if i > len(numbers):
            continue

        # find start and end postitions and create sublist
        start = position
        end = position + i

        if end <= len(numbers):
            sub_list = numbers[start:end]
            sub_list.reverse()
            numbers[start:end] = sub_list
        else:
            end = end % len(numbers)
            sub_list = numbers[start:]
            len_sub = len(sub_list)
            sub_list.extend(numbers[:end])

            sub_list.reverse()
            numbers[start:] = sub_list[:len_sub]
            numbers[:end] = sub_list[len_sub:]

        position = (position + i + skip_size) % len(numbers)
        # increment the skip_size
        skip_size += 1

    return numbers


data2 = ""


# necessary hashing functions
def sparse_hash(data, numbers, skip_size, position):
    # create new input numbers

    for i in data:
        # # check if length is greater than numbers list
        # if i > len(numbers):
        #     continue

        # find start and end postitions and create sublist
        start = position
        end = position + i

        if end <= len(numbers):
            sub_list = numbers[start:end]
            sub_list.reverse()
            numbers[start:end] = sub_list
        else:
            end = end % len(numbers)
            sub_list = numbers[start:]
            len_sub = len(sub_list)
            sub_list.extend(numbers[:end])

            sub_list.reverse()
            numbers[start:] = sub_list[:len_sub]
            numbers[:end] = sub_list[len_sub:]

        position = (position + i + skip_size) % len(numbers)
        # increment the skip_size
        skip_size += 1

    return skip_size, position, numbers


def dense_hash(numbers):
    dense = []
    for i in range(16):
        sub_hash = numbers[i * 16 : (i * 16 + 16)]
        dense.append(hex(reduce(xor, sub_hash)))
    return dense


def clean_hash(dense):
    clean = []
    for i in dense:
        temp = i[2:]
        if len(temp) == 1:
            clean.append(f"0{temp}")
        else:
            clean.append(temp)
    return "".join(clean)


def part_2(data):

    # Convert data to ASCII
    asc = []
    for i in data:
        asc.append(ord(i))

    # add values
    asc.extend([17, 31, 73, 47, 23])

    # running 64 rounds
    skip_size = 0
    position = 0
    numbers = list(
        range(256)
    )  # You need to only add this once, I misunderstood this before

    for i in range(64):
        skip_size, position, numbers = sparse_hash(asc, numbers, skip_size, position)
    # return numbers
    dense = dense_hash(numbers)
    return clean_hash(dense)


if __name__ == "__main__":
    test_numbers = [0, 1, 2, 3, 4]
    test_data = [3, 4, 1, 5]

    numbers = part_1(numbers, data)
    print(f"Answer 10a: {numbers[0] * numbers [1]}")
    print(f"Answer 10b: {part_2(data2)}")
