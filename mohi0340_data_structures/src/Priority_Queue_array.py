"""
-------------------------------------------------------
[Priority Queue]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""

from copy import deepcopy


# can be done two ways:
# queue can be sorted by priority in the queue
# can be sorted by priority when exiting the queue
class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        # create an empty list
        self._values = []
        # create first value None
        self._first = None

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        # return length of list values = 0 if its empty
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """
        # return the length of list values
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is appended to the end of the the priority queue
        Python list, and _first is updated as appropriate to the index of
        value with the highest priority.
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))

        # Determine whether new value has highest priority.
        if self._first is None:
            # if self .first is None
            # then self.first is equal to 0
            self._first = 0

        # and if value is less than the first value in self
        elif value < self._values[self._first]:
            # first value will equal the length of self._values -1
            # if length = 10
            # self. first will equal 9
            self._first = len(self._values) - 1
        # this is basically how to set an index as first
        return

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty priority queue"

        # self._first = None at beggining
        # grab value that is set to first(highest priority)
        value = deepcopy(self._values[self._first])

        return value

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty priority queue"
        # pop highest priority value
        value = self._values.pop(self._first)
        # find the value with the next highest priority
        self._set_first()

        return value

    def _set_first(self):
        """
        -------------------------------------------------------
        Private helper function to set the value of _first.
        _first is the index of the value with the highest
        priority in the priority queue. None if queue is empty.
        Use: self._set_first()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # length of self.values into variable n
        n = len(self._values)

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
                if self._values[i] < self._values[self._first]:
                    self._first = i
        return

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the priority queue
        from front to rear. Not in priority order.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The source priority queue is empty when the method
        ends. The order of the values from source is preserved.
        Use: target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data object (?)
        Returns:
            target1 - a priority queue that contains all values
                with priority higher than key (Priority_Queue)
            target2 - priority queue that contains all values with
                priority lower than or equal to key (Priority_Queue)
        -------------------------------------------------------
        """
        # assign variables as priority queues
        target1 = Priority_Queue()
        target2 = Priority_Queue()

        # while list is not empty
        while len(self._values) > 0:
            # pop the first index from self._values and put into variable v
            v = self._values.pop(0)

            # if v is less than key
            if v < key:
                # append the first index from self.values into target 1
                # append the list before the value of key into target 1
                target1._values.append(v)

            # if is greater than key
            else:
                # append the first index from self.values into target 2
                # append the list after and including the value of key into
                # target 2
                target2._values.append(v)

        # set first to None as list will be empty
        self._first = None

        # run set first function for both target 1 and target 2
        target1._set_first()
        target2._set_first()

        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a priority queue into two with values going to alternating
        priority queues. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a priority queue that contains alternating values
                from the current queue (Priority_Queue)
            target2 - priority queue that contains  alternating values
                from the current queue  (Priority_Queue)
        -------------------------------------------------------
        """
        # initialize both target 1 and target 2
        target1 = Priority_Queue()
        target2 = Priority_Queue()

        # while the first index in the list exists
        left = True

        # while the list is not empty
        while len(self._values) > 0:

            # if there is a value at index 1 in self.values
            if left:
                # remove values from self and add it to target 1
                target1._values.append(self._values.pop(0))
            else:
                # remove values from self and add it to target 2
                target2._values.append(self._values.pop(0))
            ####WHAT DOES THIS EVEN MEAN##########
            left = not left

        # set first to none when the list is empty
        self._first = None

        # run set first function for both target 1 and target 2
        target1._set_first()
        target2._set_first()

        return target1, target2

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target priority queue.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based priority queue (Priority_Queue)
            source2 - an array-based priority queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """

        # while source 1 and source 2 are not empty
        while len(source1._values) > 0 and len(source2._values) > 0:
            # remove values from source1 and source 2 and append it to
            # self.values
            self._values.append(source1._values.pop(0))
            self._values.append(source2._values.pop(0))

        # while source is not empty
        while len(source1._values) > 0:
            # remove value from source 1 and put it in self.values
            self._values.append(source1._values.pop(0))

        # while source2 is not empty
        while len(source2._values) > 0:
            # remove value from source 2 and put it in self.values
            self._values.append(source2._values.pop(0))

        # first index value in source 1 is None to make sure its empty
        source1._first = None
        # first index value in source 2 is None to make sure its empty
        source2._first = None

        # set the value of first again after this function runs
        self._set_first()
        return
