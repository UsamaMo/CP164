"""
-------------------------------------------------------
[Lab 3 Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-30"
-------------------------------------------------------
"""


from utilities import array_to_queue
from Queue_array import Queue

source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
queue = Queue()
array_to_queue(queue, source)

for i in queue:
    print(i)
