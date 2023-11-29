"""
-------------------------------------------------------
[Sorted List]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""

from copy import deepcopy

# list is sorted numerically


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: target = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._values = []

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if source contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if source contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        # search for key
        i = self._binary_search(key)

        # return key if it exists
        return i > -1

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of source.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of source (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'

        # index at self values is equal to value
        value = deepcopy(self._values[i])

        return value

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of a sorted list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in source.
        -------------------------------------------------------
        """
        # return the length of (self.values)
        return len(self._values)

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the index of the first occurrence of key in
                the list, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        # similar code to insert
        # because it uses less comparisons than a for loop
        # index 0

        #(low)first index equals 0
        low = 0
        # high(last index) equals self._values -1
        high = len(self._values) - 1

        # while low is less than high
        while low < high:
            # take (high minus low) and divide it by 2 and add low
            mid = (high - low) // 2 + low

            # if key is greater than the middle value of self values
            if key > self._values[mid]:
                # first index equals mid plus 1
                # so if [1,2,3,4,5]
                #low = 3+1
                #low = 4
                low = mid + 1
            # otherwise
            else:
                # last index equals mid
                # so 5 = mid
                high = mid
        # if low is equal to high and the first index of self is equal to key
        if low == high and self._values[low] == key:
            # low equals key
            i = low

        else:
            # key is not found
            i = -1

        return i

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(Sorted_List) to len(Sorted_List) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        # set valid to False
        valid = False

        # if length of self._values
        if (len(self._values) * -1) <= i < len(self._values):
            valid = True

        return valid

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from source.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            source contains one and only one of each value formerly present
            in source. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        clean = []

        index = 0

        for i in range(len(self._values)):
            if self._values[index] not in clean:
                clean.append(self._values[index])
                index += 1
            else:
                self._values.pop(index)
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Values are sorted.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """

        assert len(self._values) == 0, "Target list must be empty"

        while len(source1._values) > 0 and len(source2._values) > 0:

            if source1._values[0] <= source2._values[0]:
                self._values.append(source1._values.pop(0))
            else:
                self._values.append(source2._values.pop(0))

        while len(source1._values) > 0:
            self._values.append(source1._values.pop(0))

        while len(source2._values) > 0:
            self._values.append(source2._values.pop(0))
        return

    def copy(self):
        """
        ---------------------------------------------------------
        Copies the contents of this list to another sorted list.
        Use: target = source.copy()
        -------------------------------------------------------
        Returns:
            target - a sorted list containing a copy of the contents 
                of source (Sorted_List)
        -------------------------------------------------------
        """

        # make a sorted list
        target = Sorted_List()

        # iterate through every range in self.values
        for i in range(len(self._values)):
            # insert the contents of self.values into target
            # self index i is inserted into target
            # and it keeps looping so all values of self are inserted into self
            target.insert(self._values[i])

        return target

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in source.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in source (int)
        -------------------------------------------------------
        """

        # search for key
        i = self._binary_search(key)

        # length of self
        n = len(self._values)

        # if key is not found
        if i == -1:
            # key count is 0
            number = 0
        # if key is found
        else:
            # Because the list is sorted, all values with the same
            # key are lumped together.

            # key count = 1
            number = 1
            # key count adds one more as well
            i += 1

            # while key index is less than length of
            # self values and i index self values is equal to key
            while i < n and self._values[i] == key:
                # increment i
                # add i
                i += 1
                # increment number
                number += 1
        return number

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        i = self._binary_search(key)

        if i == -1:
            value = None
        else:
            value = deepcopy(self._values[i])

        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of key in source.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the location of the value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """

        return self._binary_search(key)

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in source.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        #[1,2,3,4,5,6]
        # check the midpoint of the list
        # is value less than or greater than midpoint
        # if value is less, than we do (midpoint-1)
        #

        # index 0
        low = 0
        # last index in list
        high = len(self._values) - 1

        # if low goes past high, stop the loop
        while low <= high:
            # if value is in the billions then it will take long
            # thats why this code is used instead of (high+low)//2
            mid = (high - low) // 2 + low
            # if midvalue is greater than value

            if self._values[mid] > value:
                # high will be less than one index of mid
                high = mid - 1
            else:
                # low will be greater than one index of mid
                low = mid + 1
        self._values.insert(low, value)

        return

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert len(self._values) == 0, "Target list must be empty"
        # for each value in source 1
        for value in source1:
            # if value in source 2 and value that is not in self vlaue list
            if (value in source2) and (value not in self._values):

                # first index = 0
                low = 0
                # last index = length(self) -1
                high = len(self._values) - 1

                while low <= high:
                    mid = (high - low) // 2 + low

                    if self._values[mid] > value:
                        high = mid - 1
                    else:
                        low = mid + 1
                self._values.insert(low, value)
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """

        return len(self._values) == 0

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are is_identical, i.e. same values appear
        in the same locations in both lists. (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (Sorted_List)
        Returns:
            identical - True if source contains the same values as target
                in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # if self values is equal to target values
        if self._values == target._values:

            identical = True
        else:
            identical = False

        return identical

    def max(self):
        """
        -------------------------------------------------------
        Returns the maximum value in source.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find maximum of an empty list'

        # Your code here
        # fix this
        # returns maximum number
        value = deepcopy(self._values[-1])
        return value

    def min(self):
        """
        -------------------------------------------------------
        Returns the minimum value in source.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find minimum of an empty list'

        # returns the min value
        #this is incorrect
        value = deepcopy(self._values[0])
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in source.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty list'

        # checks first value in self
        value = deepcopy(self._values[0])

        return value

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source with index i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
                args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], otherwise 
                the last value in source, value is removed from source (?)
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

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in source
        that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # search for key
        i = self._binary_search(key)

        # if key matches an index
        if i != -1:
            # pop that index that matches the key
            value = self._values.pop(i)
        else:
            # otherwise do nothing
            value = None

        # return value
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first item in source.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty list'

        # removes first item in list
        value = self._values.pop(0)

        return value

    def remove_many(self, key):
        """
        ---------------------------------------------------------
        Removes all values that match key in source.
        Use: source.remove_many(key)
        ---------------------------------------------------------
        Parameters:
            key - the key to match (?)
        Returns:
            None
        ---------------------------------------------------------
        """
        # do binary search for key
        i = self._binary_search(key)

        # set count to 0
        count = 0

        # if 1 is not -1
        if i != -1:

            count = 1
            temp = i + 1
            while (temp) < len(self._values) and self._values[temp] == key:
                temp += 1
                count += 1
            for _ in range(count):
                self._values.pop(i)
        return

    def split(self):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. source becomes empty.
        Use:  target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (Sorted_List)
            target2 - a new List with <= 50% of the original List (Sorted_List)
        -------------------------------------------------------
        """
        # length of self divided by 2
        half = len(self._values) // 2

        # make two sorted lists
        target1 = Sorted_List()
        target2 = Sorted_List()

        # go backwards
        for i in range(half - 1, -1, -1):
            # remove from self and insert at index 0 for target 2
            target2._values.insert(0, self._values.pop())
        for _ in range(len(self._values) - 1, -1, -1):
            # remove from self and insert at index 0 for target 1
            target1._values.insert(0, self._values.pop())
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. target1 contains the even indexed
        elements, target2 contains the odd indexed elements.
        source is empty after the function executes.
        (iterative version)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - the even indexed elements of the list (Sorted_List)
            target2 - the odd indexed elements of the list (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()

        while len(self._values) > 0:
            target1._values.append(self._values.pop(0))

            if len(self._values) > 0:
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
            target1 - a new List with values where func(value) is True (Sorted_List)
            target2 - a new List with values where func(value) is False (Sorted_List)
        -------------------------------------------------------
        """
        # Your code here

        return

    def split_key(self, key):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains all values < key,
        target2 all values >= key. source becomes empty. source is
        empty at end.
        Use:  target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            target1 - a new Sorted List with values < key (Sorted_List)
            target2 - a new Sorted List with values >= key (Sorted_List)
        -------------------------------------------------------
        """
        # initialize two sorted lists
        target1 = Sorted_List()
        target2 = Sorted_List()

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
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert len(self._values) == 0, "Target list must be empty"

        # for value in source 1 values
        for value in source1._values:
            # if value is not in self values
            if value not in self._values:
                # append value to self values
                self._values.append(value)
        # for value in source 2 value
        for value in source2._values:
            # if value is not in self values
            if value not in self._values:
                # first index = 0
                low = 0
                # last index = length-1
                high = len(self._values) - 1

                # while first index is lower than last index
                while low <= high:
                    # find the middle
                    mid = (high - low) // 2 + low

                    # if self values middle is greater than value
                    if self._values[mid] > value:
                        # last index = middle -1
                        high = mid - 1
                    else:
                        # otherwise first index is middle + 1
                        low = mid + 1

                self._values.insert(low, value)
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for value in source:
        -------------------------------------------------------
        Returns:
            value - the next value in source (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
