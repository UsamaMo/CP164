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

# This is used to tell you exact error instead of red Error
# Tells you invalid input instead of Red error

try:
    # cannot divide by zero
    value = 10 / 0
    number = int(input("Enter a Number: "))
    print(number)

# can print out error using variable
except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("Invalid Input")
