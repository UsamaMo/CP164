"""
-------------------------------------------------------
[Lab 10 Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-26"
-------------------------------------------------------
"""

from test_Sorts_array import SORTS, test_sort

print(
    f"n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")

for values in SORTS:
    test_sort(values[0], values[1])
