"""
-------------------------------------------------------
[Linked Queue]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-04-14"
-------------------------------------------------------
"""

from copy import deepcopy


class _Queue_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        # contains a copy of a value
        self._value = deepcopy(value)
        # link to the next node in the queue
        self._next = next_


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Values are stored in a
        linked structure.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        # set front node to None
        self._front = None
        # set Rear Node to None
        self._rear = None
        # set number of nodes in queue to 0
        self._count = 0

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
        # return count is equal to 0 if list is empty
        # cannot use len in linked list
        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
        # The queue will never be full, so always return False
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
        # returns the length of the queue
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """

        new_node = _Queue_Node(value, None)
        if self._front == None:
            self._front = new_node
            self._rear = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node
        self._count += 1
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
        assert self._front is not None, "Cannot remove from an empty queue"

        # set the value of the front node to return node (variable)
        return_node = self._front._value
        # if front node is equal to the last node in the queue
        if self._front == self._rear:
            # this means remove both those values from the queue
            # set front to None
            self._front = None
            # set rear to None
            self._rear = None

        else:
            # otherwise the front node equals the next node
            # change the node of first to second node
            self._front = self._front._next
        # remove the first node in the queue
        # lower the count of nodes in the queue by 1 after removing
        self._count -= 1
        # return the value of the front node which was removed
        return return_node

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
        assert self._front is not None, "Cannot peek at an empty queue"

        # return a copy of the value in  front node
        return deepcopy(self._front._value)

    def _move_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated.
        Use: target._move_front(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty queue"

        # if the front node is equal to None(queue is empty or is finished)
        if self._front is None:
            # set the front node of self to the front of source node
            self._front = source._front
            # sets the rear node of self to the front of self node
            self._rear = self._front
        # otherwise
        else:
            # the node after rear is equal to the front node of source
            self._rear._next = source._front
            # rear of self node is equal to the front node of source
            self._rear = source._front
        # if front node of source is EQUAL to last node in queue
        if source._front == source._rear:
            # set source front and rear to None
            source._front = None
            source._rear = None
        # otherwise if front node of source and rear are not EQUAL
        else:
            # set front node of source to the node after it
            source._front = source._front._next
        # set the node after rear to None like it should be
        self._rear._next = None
        # increase the count by 1
        self._count += 1
        # since front node is removed from Source to Target
        # remove 1 count(node)
        source._count -= 1
        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"

        # while the count of source is greater than 0
        while source._count > 0:
            # move the nodes in course 1 by 1 to target queue
            self._move_front(source)
            # count in source after every loop will be decreasing by 1,
            # after source count is less than 0, stop moving source nodes into
            # target queue
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        # combine two queues into the current target queue(self queue)
        # source 1 = Queue(1)
        # source 2 = Queue(2)

        # while source 1 is not empty or source 2 is not empty
        while source1._count > 0 or source2._count > 0:
            # if source 1 is not empty
            if source1._count > 0:
                # move the front node of source 1 into self queue
                self._move_front(source1)
            # if source 2 is not empty
            if source2._count > 0:
                # move the front node of source 2 into self queue
                self._move_front(source2)
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """

        # split self queue into 2 different queues alternating
        # output queues
        target1 = Queue()
        target2 = Queue()

        # while self is not empty
        while self._count > 0:
            # move the first node of self into target 1
            target1._move_front(self)
            # if self node is not empty
            if self._count > 0:
                # move the second node into target 2
                target2._move_front(self)
        # if the number of nodes in self is 0, because both targets will take
        # them
        if self._count == 0:
            # set rear node to None as self will be empty after target 1 and
            # target 2 will have the values
            self._rear = None

        # return alternating queues(target 1 and target 2) Queue
        return target1, target2

    def is_identical(self, target):
        """
        -------------------------------------------------------
        Determines whether two queues are identical.
        Values of self and target are compared and if all contents 
        are identical and in the same order, returns True, otherwise 
        returns False. Queues are unchanged.
        (iterative algorithm)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False 
                otherwise. (boolean)
        -------------------------------------------------------
        """
        # searches if two queues are identical
        # initialize identical as True
        identical = True
        # if the length of self and target are not equal
        if self._count != target._count:
            # both lists are not identical
            identical = False
        else:
            # otherwise if both queues have the same length
            # set current_source as the first node in self
            current_source = self._front
            # make a variable  called current_target and set it to the front
            # node of target
            current_target = target._front

            # initialize index as 0
            index = 0
            # while index is less than self count and is only identical
            while index < self._count and identical:
                # if the value in self node is not equal to the value in target
                # node
                if current_source._value != current_target._value:
                    # both queues are not identical
                    identical = False
                # move front node of self to the next node
                current_source = current_source._next
                # move front node of target to the next node
                current_target = current_target._next
                # increment the index by 1 after moving
                index += 1

            # keep looping until the index is less than the number of nodes in
            # self
        return identical

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
