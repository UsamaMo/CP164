"""
-------------------------------------------------------
[Linked Stack]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-04-11"
-------------------------------------------------------
"""

from copy import deepcopy


class _Stack_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a stack node that contains a copy of value
        and a link to the next node in the stack.
        Use: node = _Stack_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Stack node (_Stack_Node)
        Returns:
            a new _Stack_Node object (_Stack_Node)
        -------------------------------------------------------
        """

        # creates a node using a value and a pointer
        # copy value of self
        self._value = deepcopy(value)
        # set next to the next linked node
        self._next = next_

        # last node points to None


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Values are stored in a 
        linked structure.
        Use: stack = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        # top of the stack is empty initially
        self._top = None

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = stack.is_empty()
        -------------------------------------------------------
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        # Determine if the stack is empty(T/F)
        return len(self._value) == 0

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: stack.push(value)
        -------------------------------------------------------
        Parameters:
            value - value to be added to stack (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # push value onto top after created a node and adding a pointer to it
        self._top = _Stack_Node(value, self._top)
        return

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = stack.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of stack (?)
        -------------------------------------------------------
        """
        assert self._top is not None, "Cannot pop from an empty stack"

        # variable  value is equal to top of stack value
        value = self._top._value
        # top of stack value is equal to the next value
        self._top = self._top._next

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = stack.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of stack (?)
        -------------------------------------------------------
        """
        assert self._top is not None, "Cannot peek at an empty stack"

        # returns a copy of the value for top of the stack
        value = deepcopy(self._top)

        return value

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: stack.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        self._rear = self._top
        # set variable current as the front node
        current = self._top
        # set front to none
        self._top = None

        # while variable is not none
        while current is not None:
            # temporary variable equals next
            temp = current._next
            # current next equals front
            current._next = self._top
            # front equals current
            self._top = current
            # current equals temporary
            current = temp
        return

    def _move_top(self, source):
        """
        -------------------------------------------------------
        Moves the top node from the source stack to the target stack.
        The target stack contains the old top node of the source stack.
        The source stack top is updated. Equivalent of
        self.push(source.pop()), but moves nodes, not data.
        Use: target._move_top(source)
        -------------------------------------------------------
        Parameters:
            source - a linked stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._top is not None, "Cannot move the top of an empty stack"

        # temperorary node is equal to top of source stack
        temp = source._top
        # top of source stack is equal to next node
        source._top = source._top._next

        # temperoray node is equal to the top of self stack
        temp._next = self._top

        # top of self stack is equal to temperoray stack
        temp = self._top

        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked stack (Stack)
            source2 - an linked stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """

       # source1 and source 2 are 2 seperate linked stacks that are given
       # while stack 1 top is not empty and stack 2 top is not empty:
        while source1._top is not None and source2._top is not None:
            # move top of self into source 1
            self._move_top(source1)
            # move top of self into source 2
            self._move_top(source2)

        # while stack 1 top is not empty
        while source1._top is not None:
            # move the top of stack 1 into self
            self._move_top(source1)

        # while stack 2 is not empty
        while source2._top is not None:
            # move the top of stack 2 into self
            self._move_top(source2)

        # This will make it that the stack will be split and alternating each
        # node
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source stack into separate target stacks with values 
        alternating into the targets. At finish source stack is empty.
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """

        # target 1 is a stack
        target1 = Stack()
        # target 2 is another stack
        target2 = Stack()

        # while the top of self is not empty:
        while self._top is not None:

            # if the top of self is not empty:
            if self._top is not None:
                # move the top of self into target 1
                target1._move_top(self)
            if self._top is not None:
                # move the top of self into target 2
                target2._move_top(self)

        # return target
        return target1, target2

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            _value - the next value in the stack (?)
        -------------------------------------------------------
        """
        current = self._top

        while current is not None:
            yield current._value
            current = current._next
