#!/usr/bin/python3
""" Manipulate lists of ints
"""


class MyList(list):
    """ Manage a list of ints
    """
    def print_sorted(self):
        """ Print a list sorted in ascending order
        """
        print(sorted(self))
