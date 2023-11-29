"""
-------------------------------------------------------
[Lab 2 Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-23"
-------------------------------------------------------
"""

from Stack_array import Stack
from utilities import array_to_stack


stack = Stack()
source = [3, 4, 1, 7, 5, 2, 8, 9, 3]

array_to_stack(stack, source)

for i in stack:
    print(i)
