"""
-------------------------------------------------------
[Assignment 3 Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-09"
-------------------------------------------------------
"""

from Stack_array import Stack
from utilities import array_to_stack

source1 = Stack()
source2 = Stack()
source3 = Stack()
source3.push(1)
source3.push(2)
source3.push(3)
for x in source3:
    print(x)


array_to_stack(source1, [5, 8, 12, 8])
array_to_stack(source2, [3, 6, 1, 7, 9, 14])

target = Stack()

target.combine(source1, source2)

while (not target.is_empty()):
    list = target.pop()
    print(list)
