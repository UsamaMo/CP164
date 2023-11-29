"""
-------------------------------------------------------
[Lab 3 Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-30"
-------------------------------------------------------
"""


from Queue_array import Queue
from utilities import queue_to_array, array_to_queue

target = []
source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
queue = Queue()
array_to_queue(queue, source)
queue_to_array(queue, target)
print(target)
