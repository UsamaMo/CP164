"""
-------------------------------------------------------
[Assignment 1 Functions]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:            212090340
Email:    mohi0340@mylaurier.ca
__updated__ = "2022-02-11"
-------------------------------------------------------
"""

# Task 1


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    # make empty list and assign variable clean
    clean = []

    # loop through index in values
    for i in values:
        # if
        if i not in clean:
            clean.append(i)
    print(f"Cleaned: {str(clean)}")

# Task 2


def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvwl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """

    # length of string
    n = len(s)

    # initialize out
    out = ''

    # vowels array/list
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    # for loop that runs the length of string(n)
    for i in range(n):
        # if the index is not in vowels
        if s[i] not in vowels:
            # out = " + index of s
            # means that out is just empty and will add onto the index
            # to print it out
            out += s[i]
# return out because we want to return the full broken string
    return out

# Task 3


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    # read the whole file "hello"
    data = fv.read()

    # initialize all the variables
    u = 0
    l = 0
    d = 0
    w = 0
    r = 0

    # i will loop through whole file numerically
    # character by character in string for each line

    for i in data:
        # if the character is uppercase:
        if (i.isupper()):
            # add 1 to u to increase the count
            u += 1
        # if character is lowercase:
        elif (i.islower()):
            # add 1 to i to increase count for lower
            l += 1
        # if character is a number:
        elif (i.isnumeric()):
            # add 1 to d to increase count for numbers
            d += 1
        # if character is a space
        elif (i.isspace()):
            # add 1 to 3 to increase count for spaces
            w += 1
        else:
            # return remaining characters in r
            r += 1

    return u, l, d, w, r

# Task 4


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------

    """

    leap = year % 4
    not_leap = year % 100
    centurial_leap = year % 400

    if (centurial_leap == 0):
        leap_year = True
    elif (not_leap == 0 and centurial_leap != 0):
        leap_year = False
    elif (leap == 0):
        leap_year = True
    else:
        leap_year = False

    return leap_year

# Task 5


def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """

    palindrome = s.replace(" ", "")

    if s.lower() == s[::-1].lower():
        palindrome = True
    else:
        palindrome = False

    return palindrome

# Task 6


def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """

    i = 0
    md = 0

    for i in range(0, len(a) - 2):
        adj_value = a[i] - a[i + 1]
        adj_value = abs(adj_value)

        if adj_value > md:
            md = adj_value

    return md

# Task 7


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """

    b = []

    # row of original matrix
    # print 3
    row = len(a[0])

    # column of original matrix
    # print 3
    column = len(a)

    # loops through number of indexes in row(3)
    for i in range(row):
        # appends empty 3 times in b empty list
        b.append([])
        # loops through number of indexes in columns(3)
        # total times j loops is 9
        # 3 loops for every time i loops
        for j in range(column):

            # uses index of for loop and appends
            b[i].append(a[j][i])

    return b

# Task 8


def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    # initialize smallest
    smallest = a[0][0]

    # initiliaze largest
    largest = a[0][0]

    # number of values initialize
    num_values = 0

    # total count initialize
    total = 0
    for i in a:
        for j in i:
            num_values += 1
            total += j
            if j < smallest:
                smallest = j
            if j > largest:
                largest = j
    average = total / num_values

    return smallest, largest, total, average

# Task 9


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    pl = word

    i = 0
    vowels = "aeiouAEIOU"

    if word[0] in vowels:
        pl = word + "way"
    else:
        if word[0].isupper():
            while word[0] not in vowels or i >= len(word):
                i += 1
                word = word + word[0].lower()
                word = word[1:]
            pl = word + "ay"
            pl = pl[0].upper() + pl[1:]
        else:
            while word[0] not in vowels or i >= len(word):
                i += 1
                word = word + word[0]
                word = word[1:]
            pl = word + "ay"
    return pl
