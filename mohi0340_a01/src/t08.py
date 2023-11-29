"""
-------------------------------------------------------
[Assignment 1 Task 8]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""

from functions import matrix_stats

a = [[2, -3, -1], [-5, -1, -7], [-3, -10, 2], [-3, 4, -9]]

small, large, total, average = matrix_stats(a)

print(f"""Small: {small}
Large: {large}
Total: {total}
Average: {average}""")
