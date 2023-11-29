"""
-------------------------------------------------------
[List Array]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""

from copy import deepcopy


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: target = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._values = []

    def __getitem__(self, i):
        """
        -------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'

        # put a copy of self._values[i] in to variable value
        # i is an integer you can call from a testing file
        value = deepcopy(self._values[i])

        return value

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        # return the length of the list

        return len(self._values)

    def __setitem__(self, i, value):
        """
        -------------------------------------------------------
        The i-th element of list contains a copy of value. The existing
        value at i is overwritten.
        Use: source[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'

        # i is an index value that you can call from testing file
        # copy the index value from value array and insert it into
        self._values[i] = deepcopy(value)

        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        # searches for key using linear search
        i = self._linear_search(key)

        # returns true is i exists
        # greater than 1 means i is anything above 0
        return i > -1

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """

        # length of self values is in variable n
        n = len(self._values)

        # if negative length is less than or equal to i and less than self length
        # return i
        return (-1 * n) <= i < n

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of key in the list, -1 if key is not found (int)
        -------------------------------------------------------
        """

        # length of self_values
        n = len(self._values)

        # initialzie counter i
        i = 0

        # while i is less than n and index i in self does not equal to key
        # keep running the loop
        while i < n and self._values[i] != key:
            # keep running loop until key is found
            i += 1

        # if i equals length of self
        # it means loops is finished
        if i == n:
            # and key was not found
            i = -1
        # return the index of the key
        return i

    def _swap(self, i, j):
        """
        -------------------------------------------------------
        Swaps the position of two elements in the data list.
        The element originally at position i is now at position j,
        and visa versa.
        Private helper operations called only from within class.
        Use: self._swap(i, j)
        -------------------------------------------------------
        Parameters:
            i - index of one element to switch (int, 0 <= i < len(self._values))
            j - index of other element to switch (int, 0 <= j < len(self._values))
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index i'
        assert self._is_valid_index(j), 'Invalid index j'

        # swapping both values
        data1 = self._values[i]
        data2 = self._values[j]

        self._values[i] = data2
        self._values[j] = data1

        return

    def append(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: source.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        # or if you cant use insert function
        #self._values = self._values + [deepcopy(value)]

        return

    # def add1(self, value):
    #     return value + 1

    # apply uses a function like the above and implements it
    def apply(self, func):
        """
        -------------------------------------------------------
        Applies an external function to every value in list.
        Use: source.apply(func)
        -------------------------------------------------------
        Parameters:
          func - a function that takes a single value as a parameter 
              and returns a value (function)
        Returns:
            None
        -------------------------------------------------------
        """
        # for the range of self_values
        for i in range(len(self._values)):
            # an external funciton is applied to every value in list
            self._values[i] = func(self._values[i])

        return

    #
    def clean(self):
        """
        ---------------------------------------------------------
        The list contains one and only one of each value formerly present
        in the list. The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # # make empty list and assign variable clean
        # clean = []
        #
        # # loop through index in values
        # for i in range(len(self._values)):
        #     # if i is not in clean, move it to empty list
        #     # so if its a duplicate dont move it to empty list clean
        #     if i not in clean:
        #         clean.append(i)
        #
        #
        # self._values = clean

        # empty list
        clean = []

        index = 0
        # going through list backwards
        for i in range(len(self._values) - 1, -1, -1):
            # if index in self .value is not in clean
            # append that index into clean
            # and increase the index by 1 to keep doing it everytime
            # self.values is not in clean
            if self._values[index] not in clean:
                clean.append(self._values[index])
                index += 1

            # if it is in clean, just remove the index value from self.values
            else:
                self._values.pop(index)
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (List)
            source2 - an array-based list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        while len(source1._values) > 0 or len(source2._values) > 0:

            if (len(source1._values) > 0):
                value1 = source1._values.pop(0)
                self._values.append(value1)
            if (len(source2._values) > 0):
                value2 = source2._values.pop(0)
                self._values.append(value2)
        return

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        Use: target = source.copy()
        -------------------------------------------------------
        Returns:
            target - a copy of self (List)
        -------------------------------------------------------
        """
        target = deepcopy(self)

        return target

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        # store length of self._values into n
        n = len(self._values)

        # initialize i and number
        i = 0
        number = 0

        # while i is less then the length of self.values
        while i < n:
            # if self.values index i is equal to key
            if self._values[i] == key:
                # increase the count by 1
                number += 1
            # increase the increment by 1
            i += 1
        # return the number of times key appears in the list
        return number

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        value = None

        # cannot use linear search method in testing file
        # use linear search to look for key
        i = self._linear_search(key)

        # if key is found
        if i > -1:
            # self.values[key]
            # and copy that into value
            value = deepcopy(self._values[i])

        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list. (int)
        -------------------------------------------------------
        """
        # look for key
        i = self._linear_search(key)

        return i

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: source.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        self._values.insert(i, deepcopy(value))
        # if insert is not allowed
        # use
        # self._values[:] = self._values[:i] + \
        #     [deepcopy(value)] + self._values[i:]

        return

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (List)
            source2 - an array-based list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # for every value in source 1
        for value in source1:
            # if value is in source 2 and if value is not in self values
            if (value in source2) and (value not in self._values):
                # put value into self values
                self._values.append(deepcopy(value))
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """

        if len(self._values) == 0:
            return True
        else:
            return False

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are is_identical, i.e. same values 
        appear in the same locations in both lists. 
        (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """

        # checks if both lists are exactly the same
        return self._values == target._values

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find maximum of an empty list'

        # value = first element of list
        value = self._values[0]

        # if i is greater than the first index value
        # value = that value
        # return value
        for i in self._values:
            if i > value:
                value = deepcopy(i)

        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find minimum of an empty list'

        value = self._values[0]

        # if i is less than the first index value
        # value = that value
        # return value
        for i in self._values:

            if i < value:
                value = deepcopy(i)

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty list'

        # value equals a copy of the first index in self values
        value = deepcopy(self._values[0])

        return value

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            # pop the element at position i
            i = args[0]
            value = self._values.pop(i)
        else:
            # pop the last element
            value = self._values.pop()
        return value

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: source.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """

        self._values.insert(0, deepcopy(value))

        # or if you cant use insert function
        #self._values[:] = [deepcopy(value)] + self._values

        return

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        value = None

        # index is equal to key
        index = self._linear_search(key)

        # if index is basically 0 or greater
        # pop the index value that matches key variable
        if index > -1:
            # value equals the key value popped from self values
            value = self._values.pop(index)

        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty list'

        # remove first value in list
        value = self._values.pop(0)

        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: source.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # use it from the end of list backwards because otherwise
        # it will skip over the index
        # so use len(self._values-1,-1,-1):
        for i in range(len(self._values) - 1, -1, -1):
            # if self._values[i] is equal to key
            if self._values[i] == key:
                # remove key from self._values even if its multiple
                self._values.pop(i)

        return

    def reverse(self):
        """
        -------------------------------------------------------
        The contents of list are reversed in order with respect
        to their order before the operation was called.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        # not sure if you can use reverse public method
        self._values.reverse()

        return

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        # split the length in half
        half = len(self._values) // 2

        # creates 2 new empty lists
        target1 = List()
        target2 = List()

        # for in range(half)
        for i in range(half - 1, -1, -1):
            # remove self values and insert into target 2 at index 0
            target2._values.insert(0, self._values.pop())
        # for j in range(self._values)
        for j in range(len(self._values) - 1, -1, -1):
            # remove self values and insert into target 1 at index 0
            target1._values.insert(0, self._values.pop())

        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        # creates 2 new empty lists

        target1 = List()
        target2 = List()

        # while the list is not empty

        while len(self._values) > 0:
            # append the first value of self into target1
            target1._values.append(self._values.pop(0))
            # if list is not empty
            if len(self._values) > 0:
                # append the first value of self into target2
                target2._values.append(self._values.pop(0))
        return target1, target2

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = source.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        # Your code here

        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values < key,
        and target2 contains all values >= key. source is empty
        at end.
        Use: target1, target2 = source.split_key()
        -------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            target1 - a new List of values < key (List)
            target2 - a new List of values >= key (List)
        -------------------------------------------------------
        """
        # initialize two sorted lists
        target1 = List()
        target2 = List()

        # while length (self._values) is greater than 0
        while len(self._values) > 0:
            # value = first index of self._values
            value = self._values.pop(0)
            # if value is less than key
            if value < key:
                # target 1 will append value
                target1._values.append(value)

            else:
                # target 2 will append value
                target2._values.append(value)
        return target1, target2

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (List)
            source2 - an array-based list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # take everything from source 1 and then source 2 and append it in a
        # new list

        # for every value in source 1
        for value in source1._values:
            # if value is not in self._values
            if value not in self._values:
                # append value into self
                self._values.append(value)
        # for every value in source 2
        for value in source2._values:
            # if value is not already in self.values
            if value not in self._values:
                # add that value in self
                self._values.append(value)

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns:
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
