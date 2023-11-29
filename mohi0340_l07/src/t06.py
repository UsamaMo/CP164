"""
-------------------------------------------------------
[Lab 7 Task 6]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-06"
-------------------------------------------------------
"""

from List_linked import List

lst = List()

array1 = [1, 2, 2, 3, 4, 5]
print(f"List: {array1}")

for value in array1:
    lst.append(value)

lst.reverse_r()

print("Prints all values in reverse including duplicates")
for value in lst:
    print(value)
