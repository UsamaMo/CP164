"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-29"
-------------------------------------------------------
"""

from functions import reroute

opstring = input("Enter opstring: ")

values_in = [1, 2, 3, 4, 5, 6]

values_out = reroute(opstring, values_in)

print()
print(values_out)
