"""
-------------------------------------------------------
[Lab 8 Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-13"
-------------------------------------------------------
"""

from BST_linked import BST
from morse import DATA1, fill_letter_bst


bst = BST()

fill_letter_bst(bst, DATA1)

print("Letter , Morse Code")
for value in bst:
    print(value.letter, value.code)
