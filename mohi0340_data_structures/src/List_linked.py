"""
-------------------------------------------------------
[Linked Lists]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-04-14"
-------------------------------------------------------
"""

# pylint: disable=protected-access

from copy import deepcopy
from random import randint


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        # copy value of linked node
        self._value = deepcopy(value)

        # self pointer equals next node
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        # Initializes front to None
        self._front = None
        # Initializes rear to None
        self._rear = None
        # Intiliazes an empty list
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        # If front is empty, return front of the list
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        # return length of list
        return self._count

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, self._front)

        if self._rear is None:
            # List is empty - update the rear of the List..
            self._rear = node
        # Update the front of the List.
        self._front = node
        self._count += 1
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Adds a value to the end of the linked list
        self._append(value)
        return

    def insert(self, i, value):
        """
        -------------------------------------------------------
        Insert value at a given position. i is the index of the element
        before which to insert value.
        If i is outside of range of -len(list) to len(list) - 1, the value is
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Negative index adjustment.
        if i < 0:
            i = self._count + i

        if i <= 0:
            # Add value to the front of the list
            node = _List_Node(value, self._front)

            if self._rear is None:
                # List is empty - update the rear of the List..
                self._rear = node
            # Update the front of the List.
            self._front = node
        elif i >= self._count:
            # Add value to the rear of the list
            node = _List_Node(value, None)

            if self._front is None:
                # list is empty - update the front of the List.
                self._front = node
            else:
                self._rear._next = node
            # Update the rear of the List.
            self._rear = node
        else:
            # Add elsewhere in the list - not to front or rear
            j = 0
            previous = None
            current = self._front

            while j < i:
                # Find the proper location in the List
                previous = current
                current = current._next
                j += 1
            # Create the new node.
            node = _List_Node(value, current)
            previous._next = node
        # Increment the count
        self._count += 1
        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key (int)
        -------------------------------------------------------
        """
        # there is no previous node at the start before self._front
        # Initialize previous node
        previous = None

        # current is set to the first node in the linked list
        current = self._front

        # index position is 0 at start
        index = 0

        # while current node is not empty the value is not equal to key
        # stop once the the key is found
        # stop at None if key is not found
        while current is not None and current._value != key:
            # print(current._value, end=", ")

            # previous node is moved to the current node
            previous = current
            # and current node is moved to the next node
            current = current._next
            # and 1 index is added to goto the next index of the list
            index += 1

        # if current node is empty
        # if key is not found set index to negative 1
        if current is None:
            # index DNE and is at negative 1
            index = -1
        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # search list for key.
        # search for previous and current values only
        # linear search method returns three values: previous, current , index
        # Index is not required therefore its left as "_"
        previous, current, _ = self._linear_search(key)

        # if current node is empty
        if current is None:
            # Key is not found.
            value = None
        else:
            # current node value is equal to value
            value = current._value
            # decrease count of linked list by 1
            # because that key value will be removed from the linked list
            self._count -= 1

            # if previous node is empty which means if the key is the first
            # value
            if previous is None:
                # Remove the first node.
                # and set it to the next node
                self._front = self._front._next

                # if the front node is empty or DNE
                if self._front is None:
                    # List is empty, update _rear.
                    # since you are removing front node, rear node needs to be
                    # updated if there is just one node
                    self._rear = None
            else:
                # if there are values in the list and the front node is removed
                # previous node will equal the next node of current
                # if removing first node, previous will point to next of key
                # node
                previous._next = current._next

                # if the last node is being removed and previous next points to
                # None
                if previous._next is None:
                    # Last node was removed, update _rear.
                    # previous next is None so rear will be
                    # the node before None which will be previous
                    self._rear = previous
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        # front node value is set to the variable "value"
        value = self._front._value

        # front is equal to the node next to front
        self._front = self._front._next
        # remove 1 count as a node will be removed
        self._count -= 1

        # if the front node is empty
        if self._front is None:
            # Last node has been removed
            # last node will be empty as well
            self._rear = None
        # return the value of the front node that was removed
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # deletes duplicate values that match the key
        # while the front node is not empty and front node is equal to key
        while self._front is not None and self._front._value == key:
            # front node is moved to the next node
            # The front node contains the value to be removed
            self._front = self._front._next
            # list count is reduced by 1
            self._count -= 1

        # if front node is empty
        if self._front is None:
            # All nodes have been removed
            # front is equal to None as there are no nodes
            self._front = None
            # rear is also equal to none as there are no nodes
            self._rear = None
            # node count is 0
            self._count = 0
        else:
            # Remove key from the rest of the list
            # previous node is equal to front node
            previous = self._front
            # current node is equal to the next node
            current = self._front._next

            while current is not None:
                if current._value == key:
                    # Do not update previous
                    self._count -= 1
                    previous._next = current._next
                else:
                    previous = current
                current = current._next
            # Update the rear node
            self._rear = previous
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # usies linear search to find a value
        # previous and index are not needed
        _, current, _ = self._linear_search(key)

        # if the current value is not empty
        if current is not None:
            # deepcopy the value of the current node into value
            value = deepcopy(current._value)
        else:
            # otherwise there is no value
            value = None
        # return the matching value
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        # Makes sure that front node is not empty
        assert self._front is not None, "Cannot peek at an empty list"

        # copies value from front node into value variable
        value = deepcopy(self._front._value)
        # return copy of front node
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        # this method uses a linear search
        # it only needs the index number from linear search
        _, _, i = self._linear_search(key)

        # returns the index number of that key
        return i

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
        # sets variable n to the number of nodes in the list
        n = self._count
        # return the range of -n to n
        # if n = number of nodes in the list = 5
        # then the index has to be in between -5 and 5
        # for example list = [5,6,7,8,9]
        #Index = [0,1,2,3,4]
        #Index = [-5,-4,-3,-2,-1]

        # thats why index number is between -5 to 5
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        # set front node as the current variable
        current = self._front

        # if i is greater than or equal to 0
        # increment the index by 1
        if i >= 0:
            index = 0
        # if is less than 0
        # it means that the index will be the last value in the list
        elif i < 0:
            # takes the number of nodes in the linked list
            # and index is equal to negative of count
            index = -(self._count)

        # while index is less than i
        while index < i:
            # current variable equals next variable
            current = current._next
            # increment index value
            index += 1

        # copy current value into value
        value = deepcopy(current._value)

        # return that value
        return value

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        # current variable is set to the front node
        current = self._front

        # if index is less than 0
        if i < 0:
            # negative index - convert to positive

            i = self._count + i

        j = 0

        while j < i:
            current = current._next
            j += 1

        current._value = deepcopy(value)
        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        # previous and index are not needed for this method
        _, current, _ = self._linear_search(key)
        # if current value exists, return True
        # current is equal to key value
        # otherwise  it will return false
        return current is not None

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        # set front node to the maximum node
        max_node = self._front
        # current node to the next node of front
        current = self._front._next

        # while current value is not empty:
        # current keep siterating through list until it is set to None
        # while max moves only if another value is bigger equal to current
        while current is not None:
            # if front node value is less than next node value
            # front is equal to max value at beginning
            if max_node._value < current._value:
                # max equals the next value as it is bigger
                # current node is always set to the next node after max node
                max_node = current
            # since max node changed to next node
            # we change current node to next node as well
            current = current._next
        # current node keeps iterating through the whole list until it is set
        # to None

        # deepcopy the value of max node into variable max_data
        max_data = deepcopy(max_node._value)
        # return that data
        return max_data

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        # set minimum node to the front node
        min_node = self._front
        # and set current node to the next node of minimum
        current = self._front._next

        # keep looping the loop until the current node is equal to None
        # only the current node can be iterated

        while current is not None:
            # if the min node value is greater than current node value
            # set min node to current
            # while current is iterating , if it finds a value that is less than min value
            # set min value to that node
            if min_node._value > current._value:
                # set min node to current node containing smaller value
                min_node = current
            # increment current by setting current to the next node
            # everytime loop runs, if the current value is smaller or not smaller
            # the current node will goto the next ndoe
            current = current._next
        # take a copy of that minimum value and set it to variable min_data
        min_data = deepcopy(min_node._value)

        # return the minimum value
        return min_data

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        # Finds duplicates of the key value wanted
        # cannot use linear search as it is only used for finding one key value

        # initialize the number of keys found  to 0
        number = 0
        # set current node to the first node in the list
        current = self._front

        # while the current node is not set to None(list is not finished or
        # empty)

        while current is not None:
            # if key is equal to the current node
            if key == current._value:
                # increment the number of key by 1
                number += 1
            # set current to the next to keep transversing through whole list
            current = current._next

        # return the number of duplicate keys found in the list
        return number

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # set new front variable to None as the ending after last node is None
        # we have to make the node behind the first node equal to None as well
        new_front = None
        # set new rear variable to the first (front) node
        new_rear = self._front

        # TRY TO UNDERSTAND THIS LATER
        # while the front node is not None
        while self._front is not None:
            # set temp node as the node after front
            temp = self._front._next
            # set the next node of front to None(new front)
            self._front._next = new_front
            # set the next node
            new_front = self._front
            self._front = temp

        self._front = new_front
        self._rear = new_rear
        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains
        one and only one of each value formerly present in the list.
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # removes duplicate values from the sorted list
        # set key node to the first node
        key_node = self._front

        # while key node is not empty(list is not at its end or empty)
        while key_node is not None:

            # Loop through every node - compare each node with the rest
            # set previous variable to key node
            # set previous to front node(loop 1)
            previous = key_node
            # set current variable to next of key node
            # set current to second node(loop 1)
            current = key_node._next

            # while the current node is not None(list is not at its end or
            # empty)
            while current is not None:
                # Always search to the end of the list (may have > 1 duplicate)
                if current._value == key_node._value:
                    # Remove the current node by connecting the node before it
                    # to the node after it.
                    self._count -= 1
                    previous._next = current._next
                else:
                    previous = current
                # Move to the _next node.
                current = current._next
            # Update the rear
            self._rear = previous
            # Check for duplicates of the _next remaining node in the list
            key_node = key_node._next
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches args.
        Use: value = lst.pop(args)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (?)
                args[0], if it exists, is the index
        Returns:
            value - if args exists, the value at position args, otherwise the last
                value in the list, value is removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        if pln is not prn:
            # Swap only if two nodes are not the same node

            if pln is None:
                # Make r the new front
                left = self._front
                self._front = prn._next
            else:
                left = pln._next
                pln._next = prn._next

            if prn is None:
                # Make l the new front
                right = self._front
                self._front = left
            else:
                right = prn._next
                prn._next = left

            # Swap next pointers
            # lst._next, r._next = r._next, lst._next
            temp = left._next
            left._next = right._next
            right._next = temp
            # Update the rear
            if right._next is None:
                self._rear = right
            elif left._next is None:
                self._rear = left
        return

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values as
                target in the same order, otherwise False.
        -------------------------------------------------------
        """
        # if the length of list is not equal to the length of target list
        # these lists are not identical
        if self._count != target._count:
            identical = False
        # if the lengths are the same
        else:
            # set source node(variable) as the first node in self list
            source_node = self._front
            # set target node(variable) as the first node in target list
            target_node = target._front

            # while source node is not None(list hasnt ended or isnt empty) and
            # source node is equal to target node
            while source_node is not None and source_node._value == target_node._value:
                # move source node to the next node
                source_node = source_node._next
                # move target node to the next node
                target_node = target_node._next
            # keep running the loop until source node reaches None or until a
            # node value is not similar

            # if source node reaches None, then it means that both lists are
            # identical
            identical = source_node is None

        # return true if the list identical, false otherwise
        return identical

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        # splits the lists alternating

        # set target 1 to a list
        target1 = List()
        # set target 2 to a list
        target2 = List()

        # Initialize left as True
        left = True

        #
        while self._front is not None:

            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left

        return target1, target2

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"

        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
                # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                    # Value does not appear in target list.
                    self._append(value)
            source1_node = source1_node._next
        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"

        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in new list.
                self._append(value)
            source1_node = source1_node._next

        source2_node = source2._front

        while source2_node is not None:
            value = source2_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in current list.
                self._append(value)

            source2_node = source2_node._next
        return

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        # Split
        middle = self._count // 2 + self._count % 2
        prev = None
        curr = self._front

        for _ in range(middle):
            prev = curr
            curr = curr._next

        if prev is not None:
            # Break the source list between prev and curr
            prev._next = None

        # Define target1
        target1._count = middle
        target1._front = self._front
        target1._rear = prev

        # Define target2
        target2._count = self._count - middle
        target2._front = curr

        if target2._count > 0:
            target2._rear = self._rear

        # Clean up source
        self._front = None
        self._rear = None
        self._count = 0
        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values < key,
        and target2 contains all values >= key.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()

        while self._front is not None:

            if self._front._value < key:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
        return target1, target2

    def _move_front_to_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the front
        of the current List. Private helper method.
        Use: self._move_front_to_front(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        # Update the source list
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            # Clean up source list if empty.
            source._rear = None

        # Update the target list
        node._next = self._front
        self._front = node

        if self._rear is None:
            # Target list is empty
            self._rear = node
        self._count += 1
        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the rear
        of the current List. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            rs - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"

        node = source._front
        # Update the source list
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            # Clean up source list if empty.
            source._rear = None

        # Update the target list
        if self._rear is None:
            self._front = node
        else:
            self._rear._next = node

        node._next = None
        self._rear = node
        self._count += 1
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"

        while source1._front is not None and source2._front is not None:
            self._move_front_to_rear(source1)
            self._move_front_to_rear(source2)

        if source1._front is not None:
            self._append_list(source1)

        if source2._front is not None:
            self._append_list(source2)
        return

    def _append(self, value):
        """
        ---------------------------------------------------------
        Helper method to add a copy of value to the end of the List.
        Use: self._append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def _append_list(self, source):
        """
        -------------------------------------------------------
        Helper method to append the entire source list to the rear of the target list.
        The source list becomes empty.
        Use: target._append_list(source)
        -------------------------------------------------------
        Parameters:
            source - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"

        # Update the target queue
        if self._rear is None:
            # Current queue is empty.
            self._front = source._front
        else:
            self._rear._next = source._front

        self._rear = source._rear
        self._count += source._count
        # Empty the source queue.
        source._front = None
        source._rear = None
        source._count = 0
        return

    def clear(self):
        """
        -------------------------------------------------------
        Clears the linked list
        Use: source.clear()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
