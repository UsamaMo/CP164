"""
-------------------------------------------------------
[Lab 5 Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-20"
-------------------------------------------------------
"""

from functions import recurse

x = int(input("X-Coordinate: "))
y = int(input("Y-Coordinate: "))


ans = recurse(x, y)

print()
print(f"({x},{y})")

print(f"Answer: {ans}")
