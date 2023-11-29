"""
-------------------------------------------------------
[Lab 6 Task 5]
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

print("-----Peek: ")
print(new_list.peek())

print()
print("-----Remove: ")
print(new_list.remove(foods[5]))

file_variable.close()
