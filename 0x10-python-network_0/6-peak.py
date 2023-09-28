#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """function definition"""

    if len(list_of_integers) == 0:
        return (0)

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right)//2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
