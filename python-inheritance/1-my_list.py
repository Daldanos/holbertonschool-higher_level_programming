#!/usr/bin/python3
"""

Function to sort a list.

"""


class MyList(list):
    """subclass list"""
    def print_sorted(self):
        """making the sort"""
        sorted_list = sorted(self)
        print(sorted_list)
