"""
-------------------------------------------------------
[Lab 2 Task 5]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-23"
-------------------------------------------------------
"""

from copy import deepcopy
from utilities import stack_test
from Food_utilities import read_foods

file_variable = open("foods.txt", "r")

foods = read_foods(file_variable)

source = deepcopy(foods)

stack_test(source)

file_variable.close()
