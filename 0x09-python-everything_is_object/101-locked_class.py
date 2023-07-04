#!/usr/bin/python3
"""a lockedclass"""


class LockedClass:
    """defining the locked class which only allocates
    attribut if the name is first_name"""

    __slots__ = ['first_name']
