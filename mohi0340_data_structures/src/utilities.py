"""
-------------------------------------------------------
[Utilities]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""

from List_array import List
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    # while the length of variable source is greater than 0
    # means while the list is not empty
    # remove contents from source and push it onto the stack
    while len(source) > 0:
        stack.push(source.pop())
    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    # while stack is not empty

    while not stack.is_empty():

        # pop stack and insert into variable val

        value = stack.pop()

        # now insert value at index 0 in target list

        target.insert(0, value)

        # so basically this is used to take items from a stack and put it in a
        # list(target)

    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    # initiliaze the stack
    stack = Stack()

    # for values in source
    for i in source:
        # add i to stack
        stack.push(i)
        # testing peek
        peeked = stack.peek()
        print(peeked)

    # while stack is not empty
    while not stack.is_empty():
        # remove one value from stack
        stack.pop()
        # popped equals that removed value
        popped = stack.pop
        # print the removed value
        print(popped)

    return


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    # while length of source is greater than 0
    # which means queue is not empty
    while len(source) > 0:
        # remove the first index of source and insert it in queue
        # insert only takes one parameter so be careful
        queue.insert(source.pop(0))

    return


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    # whiile queue is not empty
    while not queue.is_empty():

        # remove one from queue and add it to target list
        target.append(queue.remove())

    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    # just used for testing the queue
    queue = Queue()

    # print true or false depending on if empty or not
    print(queue.is_empty())

    # inserts contents of a into queue
    array_to_queue(queue, a)
    val = input("Enter a value: ")
    # insert val into queue
    queue.insert(val)
    print()
    # check last value in peek
    print(queue.peek())
    print()
    # remove value in peek
    print(queue.remove())

    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    # while the length of source is not 0
    # which means that if the list is not empty
    while len(source) != 0:
        # remove the first index value in source
        # assign the first index value to v
        # insert the first indec value to pq
        v = source.pop(0)
        pq.insert(v)

    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    # while length of pq is greater than 0
    # which means that the list is empty

    while len(pq) > 0:
        # remove one value from pq
        # and insert that value to target
        val = pq.remove()
        target.append(val)
    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand

    # check if pq is empty true or false
    print(pq.is_empty())
    print()

    # insert a into pq
    array_to_queue(pq, a)

    # remove value from pq
    val = pq.remove()
    # insert removen value back into pq
    pq.insert(val)

    # check the highest priority value
    print(pq.peek())
    print()
    # removes the highest priority value
    print(pq.remove())

    return

# l05


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    # if source = [1,2,3,4,5]
    #(len(source)-1,-1,-1)
    #(index4, -1,-1)
    # going backwards in a list
    # start at the greatest value (5) and goto (-1) but not including, and
    # increment by -1)
    for i in range(len(source) - 1, -1, -1):
        # keep popping items from source, and insert them at index 0 in llist
        llist.insert(0, source.pop())

    return


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    # go backwards  in a list
    # keep popping items in llist and insert them into target at index 0

    for i in range(len(llist) - 1, -1, -1):

        target.insert(0, llist.pop())

    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    #source = [1,2,3,4,5]
    # used for testing lists
    # set list to List
    list = List()

    # tests for the List methods go here
    # print the results of the method calls and verify by hand

    # tests the value of source at index 2
    value = source[2]

    # remove value from list
    print(list.remove(value))

    print()

    # check if list is empty
    print(list.is_empty())

    print()

    # count the number of values in list
    print(list.count(value))

    print()

    # take values from source and append it to list
    array_to_list(list, source)

    # add value in list
    list.append(value)

    # remove value in list
    list.remove(value)

    print("List Remove:")
    # print the removed value
    print(list.remove(value))

    print()

    print("List Insert:")
    # insert the value in list at index 0
    list.insert(0, value)

    # print the inserted value in list at index 0
    print(list[0])

    print()

    print("List Empty:")
    # print true or false depending on if list is empty or not
    print(list.is_empty())

    print()

    print("List Count:")
    # print the number of values in list
    print(list.count(value))

    print()

    print("List Max:")
    # print the highest value in list
    print(list.max())

    print()

    print("List Min:")
    # print the lowest value in list
    print(list.min())

    print()

    print("List Index:")
    # print the index of the value in list
    print(list.index(value))

    print()

    print("List Find:")
    # find the value in list and print true or false

    print(list.find(value))

    return
