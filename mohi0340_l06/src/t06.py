"""
-------------------------------------------------------
[Lab 6 Task 6]
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

print(new_list[6])

new_list[6] = foods[11]

print()
print(new_list[6])

file_variable.close()
