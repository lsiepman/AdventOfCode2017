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
"""How many steps are required to carry the data from the square identified
in your puzzle input all the way to the access port?"""


# ANSWER 1
def find_matrix_size(value):
    return floor(sqrt(value)) + 1


def spiral(size):
    up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0)  # directions
    turn_right = {up: right, right: down, down: left, left: up}  # old -> new direction

    x = y = size // 2
    dx, dy = up  # initial direction
    matrix = [[None] * size for _ in range(size)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count  # visit
        # try to turn right
        new_dx, new_dy = turn_right[dx, dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (
            0 <= new_x < size and 0 <= new_y < size and matrix[new_y][new_x] is None
        ):  # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else:  # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < size and 0 <= y < size):
                return np.array(matrix)


def find_dist(square, start, matrix):
    start_loc = np.where(matrix == start)
    square_loc = np.where(matrix == square)

    start_loc = [start_loc[0][0], start_loc[1][0]]
    square_loc = [square_loc[0][0], square_loc[1][0]]

    dist = pdist([square_loc, start_loc], metric="cityblock")

    return int(dist[0])


matrix_size = find_matrix_size(square)
matrix = spiral(matrix_size)
print(f"Answer 3a: {find_dist(square, 1, matrix)}")

# GOAL 2
"""
What is the first value written that is larger than your puzzle input?
"""


# ANSWER 2
def fetch_neighbours(matrix, y, x):
    """Find all neigbouring values and add them together"""
    neighbours = []

    try:
        neighbours.append(matrix[y - 1][x - 1])
    except IndexError:
        neighbours.append(0)

    try:
        neighbours.append(matrix[y - 1][x])
    except IndexError:
        neighbours.append(0)

    try:
        neighbours.append(matrix[y - 1][x + 1])
    except IndexError:
        neighbours.append(0)

    neighbours.append(matrix[y][x - 1])
    neighbours.append(matrix[y][x + 1])

    neighbours.append(matrix[y + 1][x - 1])
    neighbours.append(matrix[y + 1][x])
    neighbours.append(matrix[y + 1][x + 1])

    return sum(neighbours)


def create_matrix(size, max_val):
    """Create the matrix described in the assignment"""
    up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0)  # directions
    turn_right = {up: right, right: down, down: left, left: up}  # old -> new direction

    x = y = size // 2
    dx, dy = up  # initial direction
    matrix = [[0] * size for _ in range(size)]

    while True:
        neighbours = fetch_neighbours(matrix, y, x)
        if neighbours == 0:
            neighbours = 1
        matrix[y][x] = neighbours
        # try to turn right
        new_dx, new_dy = turn_right[dx, dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (
            0 <= new_x < size and 0 <= new_y < size and matrix[new_y][new_x] is 0
        ):  # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else:  # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < size and 0 <= y < size):
                return np.array(matrix)

        if neighbours >= max_val:
            print(f"Answer 3b: {neighbours}")
            return np.array(matrix)


matrix = create_matrix(100, square)  # if your input was higher, make a larger matrix
