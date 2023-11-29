"""
-------------------------------------------------------
[Object Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""

from Student import Student

student1 = Student("Oscar", "Accounting", 3.1, False)
student2 = Student("Phyllis", "Business", 3.8, True)

print(student1.honor_roll())
print(student2.honor_roll())

# putting functions in classes is really useful
