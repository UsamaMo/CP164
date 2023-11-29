"""
-------------------------------------------------------
[Assignment 3 Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-29"
-------------------------------------------------------
"""
from functions import stack_combine
from Stack_array import Stack


source1 = Stack()
source2 = Stack()

list1 = [8, 12, 8, 5]

for v in list1:
    source1.push(v)
    list2 = [14, 9, 7, 1, 6, 3]
for x in list2:
    source2.push(x)
target = stack_combine(source1, source2)


for i in target:
    print(i)
