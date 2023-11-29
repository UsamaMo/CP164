"""
-------------------------------------------------------
[Stack Array]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""

from copy import deepcopy


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an is_empty stack. Data is stored in a Python list.
        Use: s = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        # creates a new empty list called _values
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Returns:
            True if the stack is empty, False otherwise
        -------------------------------------------------------
        """

        # checks the length of _values list
        # length = 0 when list is empty

        return len(self._values) == 0

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: s.push(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        # pushes the value ontop of the stack
        # since its using a copy, we will use deepcopy of the value
        # to copy the original value but not changing the original value

        return self._values.append(deepcopy(value))

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = s.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty stack"

        # removes value from the stack and puts it in value
        value = self._values.pop()

        return value

# peek is index at last [-1]
    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty stack"

        # look at last value in a list list index[-1]
        # return to value variable
        value = deepcopy(self._values[-1])

        return value

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        # runs the index of stack from top to bottom
        for value in self._values[::-1]:
            yield value

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based stack (Stack)
            source2 - an array-based stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        # while length of source 1 and source 2 are greater than 0
        # while both lists are not empty:

        while len(source1._values) > 0 and len(source2._values) > 0:
            # remove values from source 1 and add it to self._values
            self._values.append(source1._values.pop())
            # remove values from source 2 and add it to self. values
            self._values.append(source2._values.pop())

        # while length of source 1 is greater than 0:
        # while source1 is not empty:
        while len(source1._values) > 0:
            # remove values from source1 and add it to self._values
            self._values.append(source1._values.pop())

        # while length of source 2 is greater than 0:
        # while source2 is not empty:
        while len(source2._values) > 0:
            # remove values from source2 and add it to self._values
            self._values.append(source2._values.pop())
        return

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
        None
        -------------------------------------------------------
        """

        # reverses the contents of the stack
        # stack content = ._values

        # self._values.reverse()

        # method for using without reverse public method
        array = []
        for value in self._values:
            array.insert(0, value)
        self._values = array

        # or if you are not allowed to use insert
        # temp = []
        #
        # while len(self._values) > 0:
        #     temp.append(self._values.pop())
        #
        # while len(temp) > 0:
        #     self._values.append(temp.pop(0))

        return
