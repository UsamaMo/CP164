"""
-------------------------------------------------------
[Classes and Objects]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""

# with classes and objects we can create our own datatype


#"Class"  # defining what a student is


class Student:
    # inside this class we can define a bunch of attributes

    #"object"  # is an actual student

    # attributes
    # two underscores for init
    def __init__(self, name, major, gpa, is_on_probation):
        # map out attributes a student should have
        # what values will a student represent in program

        # actual objects name is going to be equal to the name
        # that they passed in

        # these are just parameters
        # self is referring to the actual object
        "name of student object will be equal to the name passed in"
        self.name = name
        "major of student object will be equal to the major passed in"
        self.major = major
        "gpa of student object will be equal to the gpa passed in"
        self.gpa = gpa

        self.is_on_probation = is_on_probation

        return
    "Now this is a student data type"
    "We can model real world objects inside a program by using classes to create data types"

    def honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
