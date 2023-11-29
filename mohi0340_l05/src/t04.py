"""
-------------------------------------------------------
[Lab 5 Task 4]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-20"
-------------------------------------------------------
"""

from functions import to_power

base = float(input("Base: "))
power = float(input("Power: "))


ans = to_power(base, power)
print()
print(f"{base:.0f}^{power:.0f} is {ans}")
