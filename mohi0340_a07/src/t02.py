"""
-------------------------------------------------------
[Assignment 7 Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-12"
-------------------------------------------------------
"""

from Food_utilities import read_foods
from Sorted_List_linked import Sorted_List


file = open("foods.txt", "rt")

foods = read_foods(file)


sorted_list = Sorted_List()

for value in foods:
    sorted_list.insert(value)
    print(value)

print()
sorted_list.insert(foods[5])


print()
print(f"{foods[-5].name} in sorted_list?: ")
print(foods[-4] in sorted_list)

print()
print(f"Index of {foods[-5].name}: ")
print(sorted_list.index(foods[-4]))

print()
print(f"{foods[-5].name} from sorted_list: ")
print(sorted_list.find(foods[-5]))

print()
print("Second Item: ")
print(sorted_list[2])

print()
print(f"First item: ")
print(sorted_list.peek())

print()
print(f"Min value: ")
print(sorted_list.min())

print()
print(f"Max value: ")
print(sorted_list.max())

print()
print(f"Remove first value :")
print(sorted_list.remove_front())


sl2 = Sorted_List()

sl3 = Sorted_List()

for value in range(5):
    sl2.insert(foods[value])


file.close()
