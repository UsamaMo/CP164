"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-09-13"
-------------------------------------------------------
"""
a = [3, 2, 1, 4, 5, 6]

n = len(a)
for i in range(1, n):
    # Walk through entire array, swap the next value into its
    # proper spot in the sorted part of a.
    j = i

    while j > 0 and a[j - 1] > a[j]:
        Sorts._swap(a, j - 1, j)
        j = j - 1

print(i)
print(j)
