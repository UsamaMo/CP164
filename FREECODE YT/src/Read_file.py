"""
-------------------------------------------------------
[Reading Files]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""
# all context of syntax file is stored in variable syntax
syntax = open("Syntax Help", "r")

# checks if file is readable
# print(syntax.readable())

# reads the file
# print(syntax.read())

# reading individual line
# print(syntax.readline())

# reads all the lines and puts in array
# print(syntax.readlines())

# prints line 2, starts from index 0
# print(syntax.readlines()[1])

# printing each line in the file
for empl in syntax.readlines():
    print(empl)

syntax.close()
