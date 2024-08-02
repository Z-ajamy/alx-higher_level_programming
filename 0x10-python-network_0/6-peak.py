#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns:
        peak of list_of_integers or None
    """
    l = 0
    h = len(list_of_integers) - 1

    while l < h:
        m = (l + h) // 2

        if list_of_integers[m] < list_of_integers[m + 1]:
            l = m + 1
        elif list_of_integers[m] < list_of_integers[m - 1]:
            h = m - 1
        else:
            return list_of_integers[m]

    return list_of_integers[l]
