"""
-------------------------------------------------------
[Assignment 7 Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-12"
-------------------------------------------------------
"""
from Food_utilities import read_foods
from List_linked import List

file = open("foods.txt", "rt")

foods = read_foods(file)

file.close()

lst = List()

for value in foods:
    lst.append(value)

print("First Item")
print(lst[0])

lst.prepend(foods[10])


lst.clean()

print()
print("Printing count of each item: ")
for value in lst:
    print(f"{value.name} {lst.count(value)}")

list2 = List()

list3 = List()

for value in range(10):
    list2.append(foods[value])

list3.combine(lst, list2)

print()
print("Item Count In List 3:")

for value in list3:
    print(f"{value.name} {list3.count(value)}")


for value in range(5, 10):
    lst.append(foods[value])

list2.intersection(lst, list3)

print()
print("Item Count In List 3:")

for value in list2:
    print(f"{value.name} {list2.count(value)}")


print()
print("Are list1 and list2 identical?: ")
print(lst.is_identical(list2))

print()
print("Removed Value: ")
print(lst.remove_front())


target1, target2 = list3.split()

print()
print("Target 1 Items Count: ")
print("Name/Count")

for value in target1:
    print(f"{value.name} {target1.count(value)}")

print()
print("Target 2 Items Count:")
print("Name/Count")

for value in target2:
    print(f"{value.name} {target2.count(value)}")

target3, target4 = target1.split_alt()

print()
print("Target 3 Items Count: ")
print("Name/Count")

for value in target3:
    print(f"{value.name} {target3.count(value)}")

print()
print("Target 4 Items Count: ")
print("Name/Count")

for value in target4:
    print(f"{value.name} {target4.count(value)}")

list3.union(target3, target4)
