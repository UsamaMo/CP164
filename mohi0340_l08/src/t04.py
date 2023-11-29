"""
-------------------------------------------------------
[Lab 8 Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-13"
-------------------------------------------------------
"""

from BST_linked import BST
from morse import DATA1, fill_code_bst


bst = BST()

fill_code_bst(bst, DATA1)

print("(Morse Code, Letter)")
for value in bst:
    print(value)
