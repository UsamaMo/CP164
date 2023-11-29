"""
-------------------------------------------------------
[Exponent Function]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-11"
-------------------------------------------------------
"""


def power(base, pow):

    result = 1

    for i in range(pow):
        result = result * base

    return result


print(power(2, 6))
