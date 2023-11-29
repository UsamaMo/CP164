"""
-------------------------------------------------------
[Assignment 6 Task 3]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-03-05"
-------------------------------------------------------
"""

from Deque_linked import Deque

queue = Deque()

print("Queue is empty: ")
print(queue.is_empty())

queue.insert_front(1)

queue.insert_rear(2)

print()
print("Length of queue: ")
print(len(queue))

print()
print("Value at Front: ")
print(queue.peek_front())

print()
print("Value at Rear: ")
print(queue.peek_rear())

print()
print("Value Removed: ")
print(queue.remove_front())

print()
print("Value Removed: ")
print(queue.remove_rear())

queue.insert_front(1)

queue.insert_rear(2)

queue.insert_rear(3)

queue.insert_rear(4)

queue._swap(queue._rear, queue._front)

print()
print("Values in queue: ")
for value in queue:
    print(value)
