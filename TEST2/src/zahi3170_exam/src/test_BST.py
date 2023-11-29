"""
-------------------------------------------------------
Simple BST testing - Exam
-------------------------------------------------------

-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from BST_linked import BST

# Constants
SEP = '-' * 60
# These values match the sample BST diagram on the exam web page:
# https://bohr.wlu.ca/cp164/exam
values = [11, 7, 6, 9, 8, 15, 12, 18]
print("BST Testing")
print()
print(SEP)
print("Test total_height")
print()
print(f"Create a BST with {values}")
bst = BST()

for v in values:
    bst.insert(v)

a = bst.preorder()
print(f"  Preorder: {a}")
th = bst.total_height()
print(f"  Height: {th}")
print(SEP)
print("Test mirror")
print()
print(f"Create a BST with {values}")
bst = BST()

for v in values:
    bst.insert(v)

a = bst.preorder()
print(f"  Preorder: {a}")
a = bst.inorder()
print(f"  Inorder: {a}")
print("Mirror the tree")
bst.mirror()
a = bst.preorder()
print(f"  Preorder: {a}")
a = bst.inorder()
print(f"  Inorder: {a}")
print(SEP)
print("Test rotate_left")
print()
print(f"Create a BST with {values}")
bst = BST()

for v in values:
    bst.insert(v)

a = bst.preorder()
print(f"  Preorder: {a}")
bst._root = bst._rotate_left(bst._root)
a = bst.preorder()
print("Rotated around 11")
print(f"  Preorder: {a}")
print(SEP)
