"""
-------------------------------------------------------
[Lab 4 Task 6]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-06"
-------------------------------------------------------
"""

from List_array import List
from utilities import array_to_list, list_to_array

llist = List()

source = [1, 2, 3, 4, 5]
target = [6, 7, 8, 9, 10]

array_to_list(llist, source)

print("Printing LList: ")

for i in llist:
    print(i)

list_to_array(llist, target)

for v in target:
    print(v)
