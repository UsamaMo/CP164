"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""


def max(num1, num2, num3):
    # we can also compare strings and booleans using these operators
    # == , != , >, >=, <, <=, True, False, and, or
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max(3, 4, 5))
