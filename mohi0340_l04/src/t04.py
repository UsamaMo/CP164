"""
-------------------------------------------------------
[Lab 4 Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-06"
-------------------------------------------------------
"""

from List_array import List

list = List()

list.append(0)

list.append(1)

list.append(2)

list.append(3)


if 3 in list:
    print("3 is contained in list")
else:
    print("Not contined in list")

print()
print("Index List:")
print(list.index(1))


print()
print("Find List:")
print(list.find(2))


print()
print("List Count: ")
print(list.count(2))

print()
print("List Min:")
print(list.min())

print()
print("List Max:")
print(list.max())
