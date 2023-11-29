"""
-------------------------------------------------------
[Lab 4 Task 7]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-06"
-------------------------------------------------------
"""

from Food_utilities import read_foods
from utilities import list_test

file = open("foods.txt", "rt")

source = read_foods(file)


list_test(source)

file.close()
