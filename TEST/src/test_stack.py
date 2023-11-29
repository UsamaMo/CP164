"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""

from Stack_array import Stack
from utilities import stack_test

target = Stack()
source1 = Stack()
source2 = Stack()


source1.push(1)
source1.push(2)
source1.push(3)
source1.push(4)
source1.push(5)

source2.push(6)
source2.push(7)
source2.push(8)
source2.push(9)


peek = source1.peek()
print(peek)


source1.pop()
r = source1.pop()
print(r)

for i in source1:
    print(i)
