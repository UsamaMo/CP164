"""
-------------------------------------------------------
Array versions of various sorts.
-------------------------------------------------------

-------------------------------------------------------
"""
# Imports
from math import log, floor


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of array-based sort operations.
    -------------------------------------------------------
    """
    # The Sorts

    @staticmethod
    def radix_string_sort(strings):
        """
        -------------------------------------------------------
        Performs a string radix sort.
        Use: Sorts.radix_string_sort(strings)
        -------------------------------------------------------
        Parameters:
            strings - an array of strings (list of str)
        Returns​​‌‌​‌​​:
            None
        -------------------------------------------------------
        """
        b_len = 27
        d = 1
        if Sorts.is_sorted_alpha(strings) is False:
            for h in range(len(min(strings, key = len))):
                buckets = [list() for _ in range(b_len)]
                for i in strings:
                    e = len(min(strings, key = len))-d
                    tmp = int((ord(i[e].lower())-96))
                    buckets[tmp].append(i)
                a = 0
                for b in range(b_len):
                    buck = buckets[b]
                    for i in buck:
                        strings[a] = i
                        a += 1
                d += 1
        return 

    @staticmethod
    def radix_sort(a):
        """
        -------------------------------------------------------
        Performs a base 10 radix sort on integers.
        Use: Sorts.radix_sort(a)
        -------------------------------------------------------
        Parameters:
            a - an array of base 10 integers (list)
        Returns​​‌‌​‌​​:
            None
        -------------------------------------------------------
        """
        if len(a) > 0:
            # Find the largest number in a.
            max_val = max(a)
            # Find the number of digits in the largest number.
            passes = floor(log(max_val, 10) + 1)

            # Create the empty buckets.
            buckets = []

            for _ in range(10):
                buckets.append([])

            for digit in range(passes):
                # Calculate the digit extraction numerator and denominator.
                d = 10 ** digit
                n = d * 10

                for v in a:
                    # Assign the array values to the appropriate bucket.
                    # Extract the individual digit.
                    i = v % n // d
                    # Add the number to the proper bucket.
                    buckets[i].append(v)

                # Put the values back into the original array.
                # Use an index i rather than append because the length of a
                # never changes.
                i = 0

                for bucket in buckets:
                    while bucket != []:
                        a[i] = bucket.pop(0)
                        i += 1
        return

    @staticmethod
    def is_sorted_alpha(strings):
        """
        -------------------------------------------------------
        Determines whether an array is sorted or not.
        Use: srtd = Sorts.is_sorted(strings)
        -------------------------------------------------------
        Parameters:
            strings - an array of strings (list of str)
        Returns​​‌‌​‌​​:
            srtd - True if contents of strings are sorted,
                False otherwise (boolean)
       -------------------------------------------------------
        """
        srtd = True
        n = len(strings)
        i = 0

        while srtd and i < n - 1:

            if strings[i].lower() <= strings[i + 1].lower():
                i += 1
            else:
                srtd = False
        return srtd
