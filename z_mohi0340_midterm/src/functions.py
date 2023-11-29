"""
-------------------------------------------------------
Midterm Functions
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:      212090340
Email:   mohi0340@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

from List_array import List

# Constants
OPERATORS = ('*', '/', '+', '-')


def pq_triage(source, key):
    """
    -------------------------------------------------------
    Removes all values from source that have a priority
    less than key.
    Use: pq_triage(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a key value (?)
    Returns‌​​​‌​‌​‌:
        None
    -------------------------------------------------------
    """
    source = Priority_Queue()
    #key is integer

    # pop the highest priority value

    i = 0
    while len(source) > 0:
        v = source[i]
        if v < key:
            source.remove(i)
        else:
            i = i + 1
    return


def purge(source, key):
    """
    -------------------------------------------------------
    Finds and removes all values in source that match key.
    Use: purge(source, key)
    -------------------------------------------------------
    Parameters:
        source - a List of values (List)
        key - a data element (?)
    Returns‌​​​‌​‌​‌:
        None
    -------------------------------------------------------
    """
    source = List()

    for i in range(len(source)):
        if i == key:
            source.remove(i)

    return


def eval_expression(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = eval_expression(string)
    -------------------------------------------------------
    Parameters:
        string - the space-separted postfix string to evaluate (str)
    Returns‌​​​‌​‌​‌:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """

    values = Stack()

    for i in range(len(string)):
        if values.isnumeric():
            answer = values.append(i)
        elif values == OPERATORS:
            remove = string.pop()
            values = values.append(remove)
            answer = values

    values[0]
    values = None

    return answer
