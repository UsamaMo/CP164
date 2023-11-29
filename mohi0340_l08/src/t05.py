"""
-------------------------------------------------------
[Lab 8 Task 5]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-13"
-------------------------------------------------------
"""

from BST_linked import BST
from morse import DATA1, fill_letter_bst, encode_morse


bst = BST()

fill_letter_bst(bst, DATA1)

print("English: ")
text = "My name is Usama Mohiuddin."
print(text)

print()

print("Morse Code: ")

print(encode_morse(bst, text))
code = encode_morse(bst, text)
print(code)
