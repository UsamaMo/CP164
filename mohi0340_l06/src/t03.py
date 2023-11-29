"""
-------------------------------------------------------
[Lab 6 Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-27"
-------------------------------------------------------
"""

from Food_utilities import read_foods
from List_linked import List


file_variable = open("foods.txt", "rt")

foods = read_foods(file_variable)


new_list = List()

for value in foods:
    new_list.append(value)

print("-----Count:")
print(new_list.count(foods[7]))

print()
print("-----Max:")
print(new_list.max())

print()
print("-----Min:")
print(new_list.min())

file_variable.close()
