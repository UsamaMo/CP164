"""
-------------------------------------------------------
[2d lists,Nested for loops]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# prints 1

# print(var[ROW][COLUMN])

# row and column start from 0
# print(number_grid[0][0])

# print 6
# print(number_grid[1][2])

# Nested for loops
for row in number_grid:
    for column in row:
        print(column)
