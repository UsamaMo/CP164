"""
-------------------------------------------------------
[Set Array]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""

"""
-------------------------------------------------------
Set_array.py
Array version of the Set ADT.
-------------------------------------------------------
Author:  
ID:      
Email:   
__updated__ = "2021-10-13"
-------------------------------------------------------
The PyDev module 'test_Set.py' contains a few sample tests for some of the Set
methods. The method 'print_set' is a testing method that shows you the complete
contents of a Set object in human-readable form and can also be used for testing.
-------------------------------------------------------
"""


from copy import deepcopy


class Set:
    """
    -------------------------------------------------------
    Data structure that contains a set of unique values,
        i.e. no values are repeated in a Set.
    Values stored in fixed-length Python list like in the Circular Queue.
        Do not use Python list methods that change the length of the list:
            append, insert, remove, pop, extend, delete
    Empty slots contain None.
    -------------------------------------------------------
    Examples of Set attributes:
        _values = [None, None, None, None], _capacity = 4, _count = 0, _first = 0
        _values = [1, None, 9, None],       _capacity = 4, _count = 2, _first = 1
        _values = [1, 3, 9, None],          _capacity = 4, _count = 3, _first = 3
        _values = [1, 4, None, 3],          _capacity = 4, _count = 3, _first = 2
        _values = [1, 4, 9, 3],             _capacity = 4, _count = 4, _first = None
    -------------------------------------------------------
    """
    # Default maximum size when capacity parameter is not provided
    DEFAULT_SIZE = 10

    def __init__(self, capacity=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Initializes an empty Set.
        Use: target = Set(capacity)
        Use: target = Set()  # uses DEFAULT_SIZE
        -------------------------------------------------------
        Parameters:
            capacity - maximum size of the set (int > 0)
        Returns​​‌​‌​​​‌:
            a new Set object (Set)
        -------------------------------------------------------
        """
        # Maximum size of Python list to store data.
        self._capacity = capacity
        # Python list that stores data - initialized to list of None.
        self._values = [None] * self._capacity
        # First available index for adding values -set to None if Set is full.
        self._first = 0
        # Number of unique values in Set. Cannot exceed _capacity.
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the set is empty. In an empty set, all slots
        in _values contain None.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns​​‌​‌​​​‌:
            True if the set is empty, False otherwise.
        -------------------------------------------------------
        """

        # if the count is 0  then self is empty

        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the set is full. In a full set, no slot
        in _values is None.
        Use: full = source.is_full()
        -------------------------------------------------------
        Returns​​‌​‌​​​‌:
            True if the set is full, False otherwise.
        -------------------------------------------------------
        """
        # if the capacity is full, then it means the count is full aswell

        return self._count == self._capacity

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of non-None values in the set.
        Use: n = len(source)
        -------------------------------------------------------
        Returns​​‌​‌​​​‌:
            the number of values in the set.
        -------------------------------------------------------
        """

        # returns the length of the array
        # count = length of self._values
        return self._count

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the occurrence of key in the set. Skips over None entries.
        (Private helper method - used only by other ADT methods.)
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns​​‌​‌​​​‌:
            i - the index of key in the set, -1 if key is not found (int)
        -------------------------------------------------------
        """

        # n is length of  list
        # n is basically count at max value
        # so if capacity is 10, count will be 10 and the length will be 10 as
        # well
        n = len(self._values)

        # initialize i for while loop
        i = 0

        # while i is less than n and while index i in self._values cannot equal key
        # i equals i +1
        # which means if key is not found run the loop
        while i < n and self._values[i] != key:
            i += 1

        # if i is equal to n
        # return i is equal to -1
        # i =-1 will mean the key is found as stated in the description
        if i == n:
            # return not found if it reaches the max
            i = -1

        # return the key

        return i

    def _set_slot(self):
        """
        -------------------------------------------------------
        Sets the value of _first, the index of the first location of None
        in _values.
        (Private helper method - used only by other ADT methods.)
        Use: self._set_slot()
        -------------------------------------------------------
        Returns​​‌​‌​​​‌:
            None
        -------------------------------------------------------
        """

        # length of self.values into variable n
        n = self._count

        # if length =0:
        if n == 0:
            # first value in list will be None
            self._first = None
        else:
            # first value in list will be 0
            self._first = 0

            # loop from range 1 to length -1
            for i in range(1, n):
                # it means that if the index value in self.value is less index value of first
                # set the smaller index value to first giving it higher
                # priority
                if self._values[i] is None:
                    self._first = i
        return

        # # puts length of list in variable n
        # n = self._count
        #
        # # if n is 0 , self._first is none
        # if n == 0:
        #     self._first = None
        # # other self._first is 0
        # else:
        #     self._first = 0
        #
        # # this means that if there is no length to the list
        # # there will be no indexes and will give None
        #
        # # but if there are indexes, then self._first is equal to 0
        #
        # return

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds value to the set at index _first.
        Use: inserted = source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns​​‌​‌​​​‌:
            inserted - True if value was added to source, False otherwise.
                value is added only if value is unique in the set (boolean)
        -------------------------------------------------------
        """

        inserted = False
        if value not in self._values:
            # this means to insert the value at index self._first
            # takes value and puts it in index
            inserted = self._values[self._first] = value
            # set a new self._first with value being None
            self._set_slot()

        return inserted

    def delete(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the set that matches key.
        Updates _first.
        Use: value = source.delete(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns​​‌​‌​​​‌:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        value = None

        index = self._linear_search(key)

        # if index is basically 0 or greater
        # pop the index value that matches key variable
        if index > -1:
            value = self._values.pop(index)

        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in the set that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns​​‌​‌​​​‌:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        value = None

        # cannot use linear search method in testing file
        i = self._linear_search(key)

        if i > -1:
            value = deepcopy(self._values[i])

        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the set contains a value matching key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns​​‌​‌​​​‌:
            True if the set contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """

        i = self._linear_search(key)

        return i > -1

    def maximum(self):
        """
        -------------------------------------------------------
        Returns a copy of the maximum value in the set.
        Use: value = source.maximum()
        -------------------------------------------------------
        Returns​​‌​‌​​​‌:
            value - a copy of the maximum value in source (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot find maximum of an empty set"

        # value = first element of list
        value = self._values[0]

        # if i is greater than the first index value
        # value = that value
        # return value
        for i in self._values:
            if i > value:
                value = deepcopy(i)

        return value

    def minimum(self):
        """
        -------------------------------------------------------
        Returns a copy of the minimum value in the set.
        Use: value = source.minimum()
        -------------------------------------------------------
        Returns​​‌​‌​​​‌:
            value - a copy of the minimum value in source (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot find minimum of an empty set"

        value = self._values[0]

        # if i is less than the first index value
        # value = that value
        # return value
        for i in self._values:

            if i < value:
                value = deepcopy(i)

        return value

    def intersection(self, source):
        """
        -------------------------------------------------------
        Returns a new set with only the values that appear in both
        self and source.
        Maximum size of target Set is the smaller of the maximum sizes of
            self and source.
        Use: target = self.intersection(source)
        -------------------------------------------------------
        Parameters:
            source - a set (Set)
        Returns​​‌​‌​​​‌:
            target - a set containing one copy of all the values
                that appear in both self and source (Set)
        -------------------------------------------------------
        Examples:
            (1,2,3) intersection (3,2,1) is (1,2,3)
            (1,2,3) intersection (4,5,6) is ()
            (1,2,3,4,5,6) intersection (0,2,4,6,8) is (2,4,6)
        -------------------------------------------------------
        """

        for value in source1:
            if (value in source2) and (value not in self._values):
                self._values.append(deepcopy(value))
        return

    def difference(self, source):
        """
        -------------------------------------------------------
        Return a set that contains the items that only exist in
        self and not in source.
        Maximum size of target Set is the maximum size of self.
        Use: target = self.difference(source)
        -------------------------------------------------------
        Parameters:
            source - a set (Set)
        Returns​​‌​‌​​​‌:
            target - a set containing one copy of all the values
                in self that are not in source (Set)
        -------------------------------------------------------
        Examples:
            (1,2,3) difference (3,2,1) is ()
            (1,2,3) difference (4,5,6) is (1,2,3)
            (1,2,3,4,5,6) difference (0,2,4,6,8) is (1,3,5)
        -------------------------------------------------------
        """
        # incomplete
        target = deepcopy(self)

        for i in range(len(target)):
            for j in range(len(source)):
                if target[i] == source[j]:
                    target.delete(target[i])

        return target

    def print_set(self):
        """
        -------------------------------------------------------
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Prints the contents of a Set in human readable format.
        Use: source.print_set()
        -------------------------------------------------------
        Returns​​‌​‌​​​‌:
            None
        -------------------------------------------------------
        """
        print(f"_values:   {self._values}")
        print(f"_capacity: {self._capacity:2d}")
        print(f"_count:    {self._count:2d}")
        print(f"_first:     {self._first:2d}")
        print("----------")
        return

    def __iter__(self):
        """
        -------------------------------------------------------
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the set
        from left to right.
        Use: for v in source:
        -------------------------------------------------------
        Returns​​‌​‌​​​‌:
            value - the next value in the set (?)
        -------------------------------------------------------
        """
        for value in self._values:
            if value is not None:
                yield value
