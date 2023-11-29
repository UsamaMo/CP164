"""
-------------------------------------------------------
[Assignment 9 Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-26"
-------------------------------------------------------
"""

from BST_linked import BST

bst = BST()

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in arr:
    bst.insert(i)

zero, one, two = bst.node_counts()

print("No Children Node Count: ")
print(zero)

print()
print("One Child Node Count: ")
print(one)

print()
print("Two Children Node Count: ")
print(two)

print()
print("Does BST contains 10?: ")
print(10 in bst)

print()
print("Parent Node for 10: ")
print(bst.parent(10))

print()
print("Parent Node for 5 (recursively): ")
print(bst.parent_r(5))
