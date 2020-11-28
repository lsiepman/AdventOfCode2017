# IMPORTS
from operator import xor
from functools import reduce

# DATA
numbers = list(range(256))
data = [189, 1, 111, 246, 254, 2, 0, 120, 215, 93, 255, 50, 84, 15, 94, 62]

# GOAL 1
"""
To achieve this, begin with a list of numbers from 0 to 255, 
a current position which begins at 0 (the first element in the list), 
a skip size (which starts at 0), and a sequence of lengths (your puzzle input). 

Then, for each length:
    Reverse the order of that length of elements in the list, starting with the element at the current position.
    Move the current position forward by that length plus the skip size.
    Increase the skip size by one.

The list is circular; if the current position and the length try to reverse elements beyond the end of the list,
 the operation reverses using as many extra elements as it needs from the front of the list. 
If the current position moves past the end of the list, it wraps around to the front. 
Lengths larger than the size of the list are invalid.
"""

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
        
        position = (position + i + skip_size) % len (numbers)
        # increment the skip_size
        skip_size +=1

    return numbers



# GOAL 2
"""
The logic you've constructed forms a single round of the Knot Hash algorithm; 
running the full thing requires many of these rounds. 
Some input and output processing is also required.

First, from now on, your input should be taken not as a list of numbers, 
but as a string of bytes instead. Unless otherwise specified, 
convert characters to bytes using their ASCII codes. 

Once you have determined the sequence of lengths to use, 
add the following lengths to the end of the sequence: 17, 31, 73, 47, 23.

Second, instead of merely running one round like you did above, 
run a total of 64 rounds, 
using the same length sequence in each round. 
The current position and skip size should be preserved between rounds.

Once the rounds are complete, you will be left with the numbers from 0 to 255 in some order, 
called the sparse hash. Your next task is to reduce these to a list of only 16 numbers called the dense hash. 
To do this, use numeric bitwise XOR to combine each consecutive block of 16 numbers in the sparse hash 
(there are 16 such blocks in a list of 256 numbers). So, the first element in the dense hash is the first 
sixteen elements of the sparse hash XOR'd together, the second element in the dense hash is the second sixteen 
elements of the sparse hash XOR'd together, etc.

Finally, the standard way to represent a Knot Hash is as a single hexadecimal string; 
the final output is the dense hash in hexadecimal notation. 
Because each number in your dense hash will be between 0 and 255 (inclusive), 
always represent each number as two hexadecimal digits (including a leading zero as necessary).
"""
data2 = "189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62"

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
        
        position = (position + i + skip_size) % len (numbers)
        # increment the skip_size
        skip_size +=1

    return skip_size, position, numbers

def dense_hash(numbers):
    dense = []
    for i in range(16):
        sub_hash = numbers[i*16:(i*16 + 16)]
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
    numbers =  list(range(256)) # You need to only add this once, I misunderstood this before 

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
