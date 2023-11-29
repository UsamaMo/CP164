"""
-------------------------------------------------------
[Queue Array]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""

from copy import deepcopy


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """

        # make an empty list for the stack
        # Stack list is stored in variable _values

        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        # return length of Stack list
        # Stack list is empty when length is 0
        return len(self._values) == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full. (Given the expandable nature
        of the Python list _values, the queue is never full.)
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
        # queue can never be full thats why return false for a queue
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """

        # return length of Stack list
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # takes value from user and appends it to Stack list
        # makes copy of the value from the user so it doesnt change
        self._values.append(deepcopy(value))

        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------
        """
        # assert means "IT HAS TO BE TRUE"
        # lenght of Stack list has to be greater than 0 to remove something
        assert len(self._values) > 0, "Cannot remove from an empty queue"

        # at front of queue, index(0) in a list, a value is popped
        # this value is stored in a variable called value
        #value is returned
        value = self._values.pop(0)

        return value

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based queue (Queue)
            source2 - an array-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        # same as stack combine
        # while both source 1 and source 2 are not empty:
        while len(source1._values) > 0 and len(source2._values) > 0:

            # remove values from source 1 and source 2 and add it to
            # self._values
            self._values.append(source1._values.pop(0))
            self._values.append(source2._values.pop(0))

        while len(source1._values) > 0:
            self._values.append(source1._values.pop(0))

        while len(source2._values) > 0:
            self._values.append(source2._values.pop(0))
        return

# peek is the index at first [0]
    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        # cannot peak if there are no values
        assert len(self._values) > 0, "Cannot peek at an empty queue"

        # copy the index value at 0 and store it into value variable
        # return variable
        value = deepcopy(self._values[0])

        return value

# used for printing out a list using for loops in testing files
    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in queue:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """

        for value in self._values:
            yield value

#
    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values
        alternating into the targets. At finish source queue is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains remaining values from source (Queue)
        -------------------------------------------------------
        """
        # create two empty queues
        # example
        # [1,2,3,4]
        # Alternating
        # target1 = [1,3]
        # target2 = [2,4]

        # create two new queues
        target1 = Queue()
        target2 = Queue()

        # if there is a value at index 0 of source then left is true
        left = True

        # if the list is not empty
        while len(self._values) > 0:

            # if there is a value at index 0 of source
            if left:
                # append that value to target1
                # so append [1] into target 1
                target1._values.append(self._values.pop(0))
            else:
                # append the next value into target 2
                # sp append[2] into target 2
                target2._values.append(self._values.pop(0))
            # MAKE SURE WHAT THIS MEANS
            left = not left
        return target1, target2

    def is_identical(self, target):
        """
        ----------------
        Determines whether two queues are identical.
        Entries of self and target are compared and if all contents are identical
        and in the same order, returns True, otherwise returns False.
        Use: identical = source.is_identical(target)
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False otherwise.
                source and target are unchanged. (boolean)
        ---------------
        """

        # check the lenght of self._values an dput into variable n
        n = len(self._values)

        # Compare the queue lengths.
        identical = n == len(target._values)
        #identical = len(self._values) == len(target._values)

        # set index counter to 0
        i = 0

        # while identical and i is less than the length of self._values
        while identical and i < n:
            # if counter i in self.values index cannot equal target . values
            # index i:
            if self._values[i] != target._values[i]:
                # identical equals false
                identical = False
            else:
                # otherwise keep adding one more to index until it reaches the
                # lenght of self.Values
                i += 1
        return identical
