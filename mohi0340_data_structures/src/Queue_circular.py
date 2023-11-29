"""
-------------------------------------------------------
[Circular Queue]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""


from copy import deepcopy

# you need to have a capcity to run this loop
# insert will goto next index when data is inserted
# fron will goto next index when data is removed
# if rear equals none you are at capacity
# so you cant add more data
# you can only remove

# DO NOT USE METHODS IN CIRCULAR QUEUE
# append,insert,remove,pop extend, delete


class Queue:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    # a default maximum size when one is not provided
    DEFAULT_CAPACITY = 10

# constructor
    def __init__(self, capacity=DEFAULT_CAPACITY):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a fixed-size list.
        Use: target = Queue(capacity)
        Use: target = Queue()  # uses default max size
        -------------------------------------------------------
        Parameters:
            capacity - maximum size of the queue (int > 0)
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
    # queue size has to be greater than 0
        assert capacity > 0, "Queue size must be > 0"
    # capacity = 10(fixed value)
        self._capacity = capacity
    #[None,None,None,None,None,None,None,None,None,None]
    # list will create 10 None types
    # None is an object which means nothing
    # None is used to fill something when the list is empty
        self._values = [None] * self._capacity
    # list is None for empty list
    # list index[0] is front if 1 value is inserted
        self._front = None   # queue has no data
    # list index[0] is rear for empty list
    # list index[1] is rear if 1 value is inserted
        self._rear = 0       # first available index for insertion
    # count is 0 because list is empty
        self._count = 0      # number of data items

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        # At beginning list is empty and should return 0
        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: full = source.is_full()
        -------------------------------------------------------
        Returns:
            True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        # did count reach capcity max
        # did count reach 10?
        return self._count == self._capacity

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in the queue.
        -------------------------------------------------------
        """
        # returns length of the count in a circular queue

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: source.insert( value )
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot add to a full queue"

        # Insert value into the queue
        self._values[self._rear] = deepcopy(value)

        # update the count
        self._count += 1

        # when the list is empty set front to none
        if self._front is None:
            # set front to what rear used to be
            self._front = self._rear

        # if data count is maxed (count =10)
        if self._capacity == self._count:

            # if capcity is full rear is none
            self._rear = None

        #capacity is 8
        # index is 7 for 8 capacity
        # in a circular queue it will max at index 7 and will never reach index 8
        # so capcity in this case is 8 and (8-1) is 7
        # so when self._rear is 7, self._rear is at the last possible index
        # self._rear = 0 and and goes to start of list
        # otherwise keep increase self._rear until it reaches the last index

        # if index equal to self.rear( meaning self rear is at max capcity)(10)
        elif (self._capacity - 1) == self._rear:
            # self._rear equals 0 capcity is full
            # and self rear cant add more
            self._rear = 0

        else:
            # otherwise keep incrementing the data count until it hits max
            # capacity(10)
            self._rear += 1

        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = source.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
                removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty queue"

        # gets the value at the front
        value = deepcopy(self._values[self._front])

        # updates the count
        self._count -= 1

        # if capacity is maxed out
        #rear is None
        # rear is place for inserting values

        # if capcity is maxed , rear is none
        #rear is front
        if self._rear is None:
            self._rear = self._front

        # if count is 0 and list is empty
        #front = None
        # because the list is empty
        if self._count == 0:
            self._front = None

        # if front = max capcity
        # front = 0
        elif self._front == (self._capacity - 1):
            self._front = 0

        else:
            # otherwise keep increasing value of front till it reaches max capacity
            #(if capcity is 8, front should reach index 7 )
            self._front += 1

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of the queue -
                the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty queue"

        # take the first index of self.values
        # copy it and put in variable value
        value = deepcopy(self._values[self._front])

        return value

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in cq:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        if self._front is not None:
            # queue is not empty
            j = self._front
            i = 0

            while i < self._count:
                yield self._values[j]
                i += 1
                j = (j + 1) % self._capacity
