"""
-------------------------------------------------------
[Chinese Chef]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""

from Chef import Chef

# inside of this chinese chef we use
"Inheritance"  # to give all of Chef functions to ChineseChef

# used for using another clas in a class


class ChineseChef(Chef):

    # overrides Chef and BBQ ribs to make orange chicken
    def make_special_dish(self):
        print("The Chinese chef makes orange chicken")

    def make_fried_rice(self):
        print("The Chinese chef makes fried rice")
