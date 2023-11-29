"""
-------------------------------------------------------
[Lab 7 Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-06"
-------------------------------------------------------
"""

from List_linked import List

lst = List()

array1 = [1, 2, 3, 5, 4]
print(f"List: {array1}")
print()

for value in array1:
    lst.append(value)

target1, target2 = lst.split_alt_r()

print("Split the list into two parts:")
print()
print("Target1: ")
for value in target1:
    print(value)

print()
print("Target2: ")
for value in target2:
    print(value)
