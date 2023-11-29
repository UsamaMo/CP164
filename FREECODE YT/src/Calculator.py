"""
-------------------------------------------------------
[Building Basic Calculator]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""


num1 = float(input("Enter first number: "))
op = input("Enter a operator: ")
num2 = float(input("Enter second number: "))

print()
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")
