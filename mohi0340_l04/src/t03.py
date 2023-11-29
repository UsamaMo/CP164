"""
-------------------------------------------------------
[Lab 4 Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-06"
-------------------------------------------------------
"""

from List_array import List

list1 = List()

print("Append: ")
list1.append(100)

for i in list1:
    print(i)

print()
print("Insert:")

list1.insert(0, 200)

for v in list1:
    print(v)

print()
print("Remove: ")
remove = list1.remove(200)

print(remove)
