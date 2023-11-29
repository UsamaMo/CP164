"""
-------------------------------------------------------
[Assignment 6 Task 1]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-05"
-------------------------------------------------------
"""

from Queue_linked import Queue

queue = Queue()

print("Queue Empty: ")
print(queue.is_empty())

print()
print("Queue Full: ")
print(queue.is_full())

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

queue1 = Queue()

queue1.insert(55)

queue2 = Queue()

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
