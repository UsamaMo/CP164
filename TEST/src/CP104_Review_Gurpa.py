"""
-------------------------------------------------------
[Cp104 Review Gurparkash]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-13"
-------------------------------------------------------
"""

# using while loop to go backward

# x = [1, 2, 3, 4, 5]
#
# index = len(x) - 1
#
# while index >= 0:
#     print(x[index])
#     index -= 1


# using while loop to go forward
# y = [1, 2, 3, 4, 5]
#
# i = 0
#
# while i >= 0:
#     print(x[i])
#     i += 1


# x = ["Hello", [4, 5, 6, 7], 6]
#
#
# #print index 1
# y = x[1]
# print(y)
#
# #print 5 from index 1
# z = x[1][1]
# print(z)
#
# #print l from hello
# a = x[0][2]
# print(a)

# # reverse a list
# x = [1, 2, 3, 4, 5, 6, 7]
# print(x[::-1])


# opening a file using a for loop
#file = open("test.txt", "rb")

# printing all characters in the file
# for x in file:
#     print(x)
#
# file.close()


# opening a file using while loop

# file = open("test.txt", "r")
#
# x = file.readline()
#
# while x.strip() != "":
#     print(x)
#     x = file.readline()
#
#
# file.close


# nested for loops
# for x in range(1,10):
#     for y in range(1,10):
#         print(x*y)
#
#     #printing a space in between the loop run
#     print()
#
# nested 2D for loop list
# x = [[1,2,3],[2,4,6]]
#
# for i in x:
#     for j in i:
#         print(x*y)


# nested while loops
# x = [[1,2,3], [2,4,6]]
#
# values = 0
# index = 0
#
#
# while values > len(x):
#     while index > x[values]:
#         print(x[values][index])
#     print()
