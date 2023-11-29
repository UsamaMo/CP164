"""
-------------------------------------------------------
[Lab 6 Task 1]
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
print("-----Append:")
new_list.append(foods[5])


new_list.prepend(foods[1])


new_list.insert(3, foods[0])

for value in new_list:
    print(value)
    print()

file_variable.close()
