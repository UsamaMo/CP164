"""
-------------------------------------------------------
[Lab 9 Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-20"
-------------------------------------------------------
"""

from Hash_Set_array import Hash_Set

hash = Hash_Set(1)

array = [1, 2, 3, 4, 5, 8, 10, 100, 950, 7, 8000]

for value in array:
    hash.insert(value)


for value in array:
    hash.insert(value + 1)
    hash.insert(value + 2)

hash.debug()
