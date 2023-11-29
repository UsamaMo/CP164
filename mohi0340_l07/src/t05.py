"""
-------------------------------------------------------
[Lab 7 Task 5]
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

lst3 = List()

array1 = [1, 2, 3, 4, 5, 1]
print(f"List1: {array1}")

array2 = [6, 7, 8, 9, 10, 9, 7]
print(f"List2: {array2}")
print()
for value in array1:
    lst1.append(value)

for value in array2:
    lst2.append(value)

lst3.union_r(lst1, lst2)

print("Prints all values while removing duplicate values:")
for value in lst3:
    print(value)
