"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-04-06"
-------------------------------------------------------
"""


def sumnums(n):
    if n == 1:
        return 1
    return n + sumnums(n - 1)


print(sumnums(3))
print(sumnums(6))
print(sumnums(9))
