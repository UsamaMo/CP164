"""
-------------------------------------------------------
[Assignment 4 Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-05"
-------------------------------------------------------
"""

from Queue_circular import Queue
from functions import queue_split_alt

source = Queue(5)
source.insert(2)
source.insert(1)
source.insert(3)
source.insert(4)
source.insert(5)

target1, target2 = queue_split_alt(source)

print("Print Target 1:")

while len(target1) > 0:
    print(target1.remove())

print()
print("Print Target 2:")
while len(target2) > 0:
    print(target2.remove())
