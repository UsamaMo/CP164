"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-20"
-------------------------------------------------------
"""

from Hash_Set_array import Hash_Set

hash = Hash_Set(10)

hash.insert(1)

hash.insert(2)

hash.insert(3)

removed = hash.remove(2)


print("Removed Value: ")
print(removed)

print()
print("Printing Hash: ")
for value in hash:
    print(value)
