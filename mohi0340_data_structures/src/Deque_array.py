"""
-------------------------------------------------------
[Deque Array]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-04-06"
-------------------------------------------------------
"""

from copy import deepcopy


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: deque = Deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        # starts off with an empty list
        self._values = []

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of _values in the deque (int)
        -------------------------------------------------------
        """

        # returns the length of the list
        return len(self._values)

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index _values can be positive or negative and range from
          -len(deque) to len(deque) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        # initialize valid to false
        valid = False

        #(multiply length of self_values  by -1)
        # if its is less than or equal to i and if i is less than the length of(self._values)
        # it means that i has to be in between negative self and postive self

        if (len(self._values) * -1) <= i < len(self._values):
            valid = True

        return valid

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps _values of two nodes within a deque. l has taken the place of r, 
        r has taken the place of l.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - an index of a deque value (int)
            r - an index of a deque value (int)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._is_valid_index(l) and self._is_valid_index(
            r), "indices to swap must be valid"

        data = self._values[l]
        data2 = self._values[r]

        self._values[r] = data
        self._values[l] = data2

        return

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        deepcopy(self._values.insert(0, value))

        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.insert(len(self._values), deepcopy(value))

        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """

        return len(self._values) == 0

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty deque'

        value = deepcopy(self._values[0])

        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty deque'

        value = deepcopy(self._values[-1])

        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty deque'

        value = self._values.pop(0)

        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty deque'

        value = self._values.pop(-1)

        return value

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for value in deque:
        -------------------------------------------------------
        Returns:
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
