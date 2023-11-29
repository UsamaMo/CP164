"""
-------------------------------------------------------
[Lab 8 Task 6]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-13"
-------------------------------------------------------
"""

from BST_linked import BST
from morse import DATA1, fill_code_bst, decode_morse

bst = BST()

fill_code_bst(bst, DATA1)

print("Morse Code: ")
text = "... --- ..."
print(text)

print()
print("English: ")
print(decode_morse(bst, text))
