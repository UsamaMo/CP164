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


def sumdigits(no):
    if no == 0:
        return 0
    else:
        return int(no % 10) + sumdigits(int(no / 10))


print(sumdigits(123))
