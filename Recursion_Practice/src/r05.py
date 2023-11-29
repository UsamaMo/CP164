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


def power(num, topwr):
    if topwr == 0:
        return 1
    else:
        return num * power(num, topwr - 1)


print('{} to the power of {} is {}'. format(4, 7, power(4, 7)))
print(power(4, 7))
