"""
-------------------------------------------------------
[Assignment 2 Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-21"
-------------------------------------------------------
"""

from Food import Food
from Food_utilities import read_foods, food_table

file_variable = open("foods.txt", "r")

foods = read_foods(file_variable)


food_table(foods)
