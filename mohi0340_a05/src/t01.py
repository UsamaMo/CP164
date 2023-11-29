"""
-------------------------------------------------------
[Assignment 5 Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-12"
-------------------------------------------------------
"""

from Food import Food
from Food_utilities import read_food, read_foods
from List_array import List
from utilities import array_to_list


# Prepare a List

# Open the food.txt file_variable
file_variable = open("foods.txt", "rt")

# Use the read_foods method to get a list of foods
foods = read_foods(file_variable)

# Close the file_variable
file_variable.close()

# Create an empty list
list1 = List()

# Add all the food items into the list
array_to_list(list1, foods)


burger = Food("Canuck Burger", 0, False, 7500)

# Use the append method
list1.append(burger)


for value in list1:
    print(f"{value.name} = {list1.count(value)}")


list1.clean()


print()
print("Printing...")
for value in list1:
    print(f"{value.name} = {list1.count(value)}")


temp = [
    read_food("Gulab Jamun|2|True|300"),
    read_food("Burrito|4|False|200")
]


list2 = List()

list2.append(temp[0])

list2.append(temp[1])


union_list = List()


union_list.combine(list1, list2)


print()
print("Printing...")
for value in union_list:
    print(f"{value.name}")


print()
print("Printing...")
print(union_list[10])


list2.append(temp[0])

list2.append(temp[1])


list4 = List()


list4.intersection(list2, union_list)


print()
print("Printing...")
for value in list4:
    print(f"{value.name}")


print()
print("Printing...")
print(list4.is_identical(list2))


list4.prepend(temp[0])


print("Printing...")
for value in list4:
    print(f"{value.name}")


list4.remove_front()

print()
print("Printing...")
for value in list4:
    print(f"{value.name}")


list4.append(temp[0])


list4.remove_many(temp[0])


print()
print("Printing...")
for value in list4:
    print(f"{value.name}")


target1, target2 = union_list.split()


print()
print("Printing...")
for value in target1:
    print(f"{value.name}")

print()
print("Printing...")
for value in target2:
    print(f"{value.name}")


target3, target4 = target1.split_alt()


print()
print("Printing...")
for value in target3:
    print(f"{value.name}")


print()
print("Printing...")
for value in target4:
    print(f"{value.name}")


union_list.union(target3, target4)


print()
print("Printing...")
for value in union_list:
    print(f"{value.name}")
