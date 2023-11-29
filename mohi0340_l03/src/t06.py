"""
-------------------------------------------------------
[Lab 3 Task 6]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-30"
-------------------------------------------------------
"""

from Food_utilities import read_foods
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array, priority_queue_test


pq = Priority_Queue()

source = [1, 2, 5, 3, 8, 6, 9, 7, 10, 4]

array_to_pq(pq, source)

while len(pq) > 0:
    val = pq.remove()
    print(val)
    source.append(val)

array_to_pq(pq, source)

pq_to_array(pq, source)

print(source)
print()

file_variable = open("foods.txt", "r")

a = read_foods(file_variable)

file_variable.close()

priority_queue_test(a)
