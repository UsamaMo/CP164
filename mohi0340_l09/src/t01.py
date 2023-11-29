"""
-------------------------------------------------------
[Lab 9 Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-20"
-------------------------------------------------------
"""

from Food_utilities import get_food
from functions import hash_table


food1 = get_food()
print()
food2 = get_food()

print()
hash_table(4, [food1, food2])
