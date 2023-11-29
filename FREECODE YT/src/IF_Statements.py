"""
-------------------------------------------------------
[If Statements]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""

is_male = True
#is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a male or tall or both")
# not(var) is used for not condition
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male nor tall")
