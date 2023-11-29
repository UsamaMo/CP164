"""
-------------------------------------------------------
[Lab 7 Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-06"
-------------------------------------------------------
"""

from List_linked import List

lst1 = List()

lst2 = List()

array1 = [1, 2, 3, 4, 5]
print(f"List 1: {array1}")


array2 = [5, 4, 3, 2, 1]
print(f"List 1: {array2}")

for value in array1:
    lst1.append(value)


for value in array2:
    lst2.append(value)

print()
print("Is the List Identical?, (T/F)")
print(lst1.is_identical_r(lst2))
