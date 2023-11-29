"""
-------------------------------------------------------
[Assignment 2 Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-22"
-------------------------------------------------------
"""

from Food import Food
from Food_utilities import read_foods, average_calories

file_variable = open("foods.txt", "r")

foods = read_foods(file_variable)

avg = average_calories(foods)

print(f"Average Calories of all foods : {avg}")
