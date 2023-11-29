"""
-------------------------------------------------------
[Assignment 4 Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-05"
-------------------------------------------------------
"""

from Priority_Queue_array import Priority_Queue
from functions import pq_split_key

source = Priority_Queue()
source.insert(4)
source.insert(3)
source.insert(2)
source.insert(1)
source.insert(5)


target1, target2 = pq_split_key(source, 3)


print("Print Target 1:")
for i in target1:
    print(i)

print()
print("Print Target 2:")
for v in target2:
    print(v)
