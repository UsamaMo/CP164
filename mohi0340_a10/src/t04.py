"""
-------------------------------------------------------
[Assignment 10 Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-04-01"
-------------------------------------------------------
"""

from Deque_linked import Deque
from Sorts_Deque_linked import Sorts


array = [15, 54, 23, 2, 44, 80, 24, 66, 73, 33]

a = Deque()

for value in array:
    a.insert_rear(value)

Sorts.gnome_sort(a)

for value in a:
    print(value, end=", ")
