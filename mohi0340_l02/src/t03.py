"""
-------------------------------------------------------
[Lab 2 Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-23"
-------------------------------------------------------
"""

from Stack_array import Stack
from utilities import stack_to_array, array_to_stack

target = []
stack = Stack()
source = [3, 4, 1, 7, 5, 2, 8, 9, 3]

array_to_stack(stack, source)
stack_to_array(stack, target)


print(target)
