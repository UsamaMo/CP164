"""
-------------------------------------------------------
[Student]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""

# from Student file import Student Class
from Student import Student

# creating a student object
# used to call function __init__
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print("Student 1")
print(student1.name)
print(student1.major)
print(student1.gpa)
print(student1.is_on_probation)

print()
print("Student 2")
print(student2.name)
print(student2.major)
print(student2.gpa)
print(student2.is_on_probation)


"an object is just an instance of a class"
