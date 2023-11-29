"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-04-08"
-------------------------------------------------------
"""

# function for calculating factorials


def factorial(n):
    # if the number is greater than 1
    if n > 1:
        # multiply the number by a number less than it
        # 5 x 4 in this case
        return n * factorial(n - 1)
    elif n == 0:
        return 1
    # return n
    return n


print(factorial(5))
