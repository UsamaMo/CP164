"""
-------------------------------------------------------
[Lab 1 Task 5]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-16"
-------------------------------------------------------
"""

from Food_utilities import read_foods

file_variable = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(file_variable)

for i in foods:
    print(i)
