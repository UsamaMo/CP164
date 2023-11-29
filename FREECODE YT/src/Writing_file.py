"""
-------------------------------------------------------
[Appending/Writing File]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""
# appends a line to the original file
# thats why there is not input
# appending to a file
# syntax = open("Syntax Help", "a")
# syntax.write("\nAppend")

# reading file
# print(syntax.read())

# will write to the file mentioned
# creates another file depending on file name
# syntax = open("Syntax Help 2", "w")
# syntax.write("\nWrite")
# syntax.close()


# creating webpages
webpage = open("index.html", "w")
webpage.write("<p>This is HTML</p>")

webpage.close()
