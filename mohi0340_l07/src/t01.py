"""
-------------------------------------------------------
[Lab 7 Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-06"
-------------------------------------------------------
"""

from List_linked import List

lst = List()

list = [1, 2, 3, 4, 5]
print(f"List: {list}")


for n in list:
    lst.append(n)

print()
print("Linear Search:")
p, c, i = lst._linear_search_r(4)

print(p._value)
print(c._value)
print(i)
