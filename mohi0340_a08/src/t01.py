"""
-------------------------------------------------------
[Assignment 8 Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-19"
-------------------------------------------------------
"""

from BST_linked import BST

bst = BST()

arr = [5, 4, 6, 7, 9, 0, 5, 9]

for value in arr:
    bst.insert(value)

print("Valid? ")
print(bst.is_valid())

print()
print("Balanced? ")
print(bst.is_balanced())

bst2 = BST()

for value in [1, 2, 3, 4, 5]:
    bst2.insert(value)

print()
print("Identical? ")
print(bst.is_identical(bst2))

print()
print("Min: ")
print(bst.min())

print()
print("0 children count: ")
print(bst.leaf_count())

print()
print("1 children count: ")
print(bst.one_child_count())

print()
print("2 children count: ")
print(bst.two_child_count())

print()
print("Values in order: ")
print(bst.inorder())

print()
print("Values in preorder: ")
print(bst.preorder())

print()
print("Values in postorder: ")
print(bst.postorder())

print()
print("Values in levelorder:  ")
print(bst.levelorder())

print()
print("Removed Value: ")
print(bst.remove(2))

print()
print("Updated List: ")
for value in bst:
    print(value)
