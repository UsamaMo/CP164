"""
-------------------------------------------------------
[Assignment 4 Task 5]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-05"
-------------------------------------------------------
"""

from Priority_Queue_array import Priority_Queue

source = Priority_Queue()
source.insert(3)
source.insert(1)
source.insert(2)
source.insert(1)
source.insert(4)
target_1, target_2 = source.split_key(3)


print("Print Target 1:")
while len(target_1) > 0:
    print(target_1.remove())

print()
print("Print Target 2:")
while len(target_2) > 0:
    print(target_2.remove())
