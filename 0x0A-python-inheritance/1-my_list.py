#!/usr/bin/python3
"""All about inheritance"""


class MyList(list):
    """Returning for the built-in list class.Sorted"""

    def print_sorted(self):
        """Print sorted in ascending order"""
        print(sorted(self))
