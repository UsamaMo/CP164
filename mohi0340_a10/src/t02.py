"""
-------------------------------------------------------
[Assignment 10 Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-04-01"
-------------------------------------------------------
"""

from List_linked import List
from Sorts_List_linked import Sorts


array = [15, 54, 23, 2, 44, 80, 24, 66, 73, 33]

a = List()

for value in array:
    a.append(value)

Sorts.radix_sort(a)

for value in array:
    print(value, end=", ")
