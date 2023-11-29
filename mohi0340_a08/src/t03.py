"""
-------------------------------------------------------
[Assignment 8 Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-19"
-------------------------------------------------------
"""

from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, letter_table


DATA = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst = BST()

for value in DATA:
    letter = Letter(value)
    bst.insert(letter)

file = open('gibbon.txt', 'rt')

do_comparisons(file, bst)

file.close()

letter_table(bst)
