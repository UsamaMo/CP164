"""
-------------------------------------------------------
[Assignment 3 Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-01-29"
-------------------------------------------------------
"""


from Stack_array import Stack


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()

    both_empty = source1.is_empty() and source2.is_empty()

    i = 1

    while not both_empty:
        if i % 2 != 0:
            if not source1.is_empty():
                target.push(source1.pop())
            else:
                target.push(source2.pop())
        else:
            if not source2.is_empty():
                target.push(source2.pop())
            else:
                target.push(source1.pop())
        i += 1

        both_empty = source1.is_empty() and source2.is_empty()

    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """

    empty = Stack()
    clear = Stack()

    while not source.is_empty():
        empty.push(source.pop())

    while not empty.is_empty():
        clear.push(empty.pop())

    while not clear.is_empty():
        source.push(clear.pop())
    return


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """

    stack = Stack()
    reverse = len(string) - 1

    j = 0

    palindrome = True
    add = True

    while j < len(string) and reverse > 0 and palindrome:
        if string[j].isalpha() and add:
            stack.push(string[j].lower())
        elif string[reverse].isalpha() and add:
            reverse += 1
        else:
            add = True
        if reverse < len(string):
            if string[reverse].isalpha():
                if (not stack.is_empty()):
                    if string[reverse].lower() != stack.pop():
                        palindrome = False
            elif string[j].isalpha():
                add = False
                j -= 1
        reverse -= 1

        j += 1

    return palindrome


def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """

    values_out = []
    stack = Stack()

    for s in opstring:
        if s == 'S':
            if(len(values_in) == 0):
                values_out = None
            else:
                stack.push(values_in.pop(0))
        elif s == "X":
            if(stack.is_empty()):
                values_out = None
            else:
                values_out.append(stack.pop())

    return values_out
