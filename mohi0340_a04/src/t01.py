"""
-------------------------------------------------------
[Assignment 4 Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-05"
-------------------------------------------------------
"""

from Queue_circular import Queue

source1 = [1, 2, 3, 4, 5]
source2 = [6, 7, 8, 9]
capacity = 5

queue = Queue(capacity)

for i in range(len(source1)):
    value = source1[i]

    queue.insert(value)

print(f"Queue: {queue._values}")
print()

for _ in range(capacity - 1):
    val = queue.remove()

print()

for i in range(len(source2)):
    value = source2[i]
    queue.insert(value)
    print(f"Add {value}")

    print()
    print(f"After: {queue._values}")

print()
print(f"Queue: {queue._values}")
