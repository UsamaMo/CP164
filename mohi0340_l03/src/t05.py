"""
-------------------------------------------------------
[Lab 3 Task 5]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-30"
-------------------------------------------------------
"""

from Priority_Queue_array import Priority_Queue
from utilities import queue_to_array, array_to_queue

target = []
source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pq = Priority_Queue()
array_to_queue(pq, source)
queue_to_array(pq, target)

print(target)
