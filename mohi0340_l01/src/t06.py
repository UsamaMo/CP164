"""
-------------------------------------------------------
[Lab 1 Task 6]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-16"
-------------------------------------------------------
"""

from Food_utilities import read_foods

from Food_utilities import write_foods

from Food import Food

file_variable = open("foods.txt", "r")

foods = read_foods(file_variable)

file_variable = open("new_foods.txt", "w")

write_foods(file_variable, foods)
