"""
-------------------------------------------------------
[Lab 3 Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-30"
-------------------------------------------------------
"""

from Queue_array import Queue
from utilities import array_to_queue, queue_to_array, queue_test

queue = Queue()

source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

array_to_queue(queue, source)
print()

for i in range(len(queue)):
    val = queue.remove()
    print(val)
    source.append(val)

array_to_queue(queue, source)
queue_to_array(queue, source)

print(source)

queue_test(source)
