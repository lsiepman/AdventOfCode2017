# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:45:34 2020.

@author: laura
"""

# IMPORTS
from math import floor, sqrt
import numpy as np
from scipy.spatial.distance import pdist


# DATA
square = 312051

# GOAL 1
"""Each square on the grid is allocated in a spiral pattern starting at a
location marked 1 and then counting up while spiraling outward.
While this is very space-efficient (no squares are skipped),
requested data must be carried back to square 1
(the location of the only access port for this memory system)
by programs that can only move up, down, left, or right.
They always take the shortest path: the Manhattan Distance between
the location of the data and square 1.

How many steps are required to carry the data from the square identified
in your puzzle input all the way to the access port?"""

# ANSWER 1
def find_matrix_size(value):
    return floor(sqrt(value)) + 1

def spiral(size):
    up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
    turn_right = {up: right, right: down, down: left, left: up} # old -> new direction

    x = y = size // 2
    dx, dy = up # initial direction
    matrix = [[None] * size for _ in range(size)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count # visit
        # try to turn right
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < size and 0 <= new_y < size and
            matrix[new_y][new_x] is None): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < size and 0 <= y < size):
                return np.array(matrix)

def find_dist(square, start, matrix):
    start_loc = np.where(matrix == start)
    square_loc = np.where(matrix == square)

    start_loc = [start_loc[0][0], start_loc[1][0]]
    square_loc = [square_loc[0][0], square_loc[1][0]]

    dist = pdist([square_loc, start_loc], metric = "cityblock")

    return int(dist[0])

matrix_size = find_matrix_size(square)
matrix = spiral(matrix_size)
print(f"Answer 3a: {find_dist(square, 1, matrix)}")

# GOAL 2
"""As a stress test on the system, the programs here clear the grid and then
 store the value 1 in square 1. Then, in the same allocation order as shown
 above, they store the sum of the values in all adjacent squares, including
 diagonals.

So, the first few squares' values are chosen as follows:

- Square 1 starts with the value 1.
- Square 2 has only one adjacent filled square (with value 1),
 so it also stores 1.
- Square 3 has both of the above squares as neighbors and stores the sum
 of their values, 2.
- Square 4 has all three of the aforementioned squares as neighbors and
 stores the sum of their values, 4.
- Square 5 only has the first and fourth squares as neighbors,
so it gets the value 5.

Once a square is written, its value does not change.
What is the first value written that is larger than your puzzle input?
"""

# ANSWER 2
def fetch_neighbours(matrix, y, x):
    """Find all neigbouring values and add them together"""
    neighbours = []
    
    try:
        neighbours.append(matrix[y-1][x-1])
    except IndexError:
        neighbours.append(0)
    
    try:
        neighbours.append(matrix[y-1][x]) 
    except IndexError:
        neighbours.append(0)
    
    try:
        neighbours.append(matrix[y-1][x+1])
    except IndexError:
        neighbours.append(0)

    neighbours.append(matrix[y][x-1])
    neighbours.append(matrix[y][x+1])

    neighbours.append(matrix[y+1][x-1])
    neighbours.append(matrix[y+1][x])
    neighbours.append(matrix[y+1][x+1])

    return sum(neighbours)


def create_matrix(size, max_val):
    """Create the matrix described in the assignment"""
    up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
    turn_right = {up: right, right: down, down: left, left: up} # old -> new direction

    x = y = size // 2
    dx, dy = up # initial direction
    matrix = [[0] * size for _ in range(size)]

    while True:
        neighbours = fetch_neighbours(matrix, y, x)
        if neighbours == 0:
            neighbours = 1
        matrix[y][x] = neighbours
        # try to turn right
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < size and 0 <= new_y < size and
            matrix[new_y][new_x] is 0): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < size and 0 <= y < size):
                return np.array(matrix)
         
        if neighbours >= max_val:
            print(f"Answer 3b: {neighbours}")
            return np.array(matrix)

matrix = create_matrix(100, square) #if your input was higher, make a larger matrix
