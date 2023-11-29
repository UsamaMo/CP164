"""
-------------------------------------------------------
[Assignment 6 Task 2]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-05"
-------------------------------------------------------
"""

from Priority_Queue_linked import Priority_Queue

queue = Priority_Queue()

print("Queue is empty: ")
print(queue.is_empty())

print()
print("Length of queue: ")
print(len(queue))

queue.insert(5)

print()
print("Length of queue: ")
print(len(queue))

queue.insert(10)

print()
print("Removed Node: ")
print(queue.remove())

print()
print("First item in queue: ")
print(queue.peek())

queue1 = Priority_Queue()

queue1.insert(4)

queue2 = Priority_Queue()

queue2.combine(queue, queue1)

print()
print("Queue 2: ")
for value in queue2:
    print(value)

target1, target2 = queue2.split_alt()

print()
print("Target 1: ")
for value in target1:
    print(value)

print()
print("Target 2: ")
for value in target2:
    print(value)

queue2.insert(5)

queue2.insert(10)

queue2.insert(15)

queue2.insert(20)

target3, target4 = queue2.split_key(40)

print()
print("Target 1: ")
for value in target3:
    print(value)

print()
print("Target 2: ")
for value in target4:
    print(value)
