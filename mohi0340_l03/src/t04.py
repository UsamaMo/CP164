"""
-------------------------------------------------------
[Lab 3 Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-10"
-------------------------------------------------------
"""


from utilities import array_to_queue
from Priority_Queue_array import Priority_Queue

source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pq = Priority_Queue()
array_to_queue(pq, source)

for i in pq:
    print(i)
