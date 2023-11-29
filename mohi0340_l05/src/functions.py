"""
-------------------------------------------------------
[Lab 5 Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-27"
-------------------------------------------------------
"""

# Task 1


def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    # If x is less than 0 or y is less than 0
    if x < 0 or y < 0:
        # subtract y from x
        ans = x - y
    else:
        # otherwise
        ans = recurse(x - 1, y) + recurse(x, y - 1)
    return ans

# Task 2


def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    # if the remainder of m divided by m is equal to zero
    if m % n == 0:
        # ans variable equals n
        ans = n

    else:
        # otherwise ans variable equals
        ans = gcd(n, m % n)

    return ans

# Task 3


def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels = "aeiouAEIOU"

    if s == "":
        count = 0

    elif s[0].lower() in vowels:
        count = 1 + vowel_count(s[1:])

    else:
        count = vowel_count(s[1:])

    return count

# Task 4


def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """

    if power == 0:
        ans = 1

    elif power > 0:
        ans = base * to_power(base, power - 1)

    else:
        ans = 1 / (base * to_power(base, abs(power) - 1))

    return ans

# Task 5


def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    length = len(s)

    if s != "":
        if s[0].isalpha() and s[-1].isalpha():
            if s[0].lower() != s[-1].lower():
                palindrome = False
            else:
                if length > 1:
                    palindrome = is_palindrome(s[1:-1])
                else:
                    palindrome = True
        elif s[0].isalpha():
            if length > 1:
                palindrome = is_palindrome(s[:-1])
            else:
                palindrome = True
        else:
            if length > 1:
                palindrome = is_palindrome(s[1:])
            else:
                palindrome = True
    else:
        palindrome = True
    return palindrome

# Task 6


def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """

    new_set = []
    if bag != []:
        if bag[-1] in bag[:-1]:
            new_set = bag_to_set(bag[:-1])
        else:
            new_set = bag_to_set(bag[:-1]) + [bag[-1]]

    return new_set
