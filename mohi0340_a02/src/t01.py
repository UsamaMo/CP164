"""
-------------------------------------------------------
[Assignment 2 Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-22"
-------------------------------------------------------
"""

from Food import Food
from Food_utilities import read_foods, by_origin

file_variable = open("foods.txt", "r")

foods = read_foods(file_variable)

print(Food.origins())
origin = int(input("Enter the Origin: "))

v = by_origin(foods, origin)


for i in v:
    print(i)
    print()

file_variable.close()
