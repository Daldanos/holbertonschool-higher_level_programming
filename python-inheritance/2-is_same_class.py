#!/usr/bin/python3
"""

Function to check if is the same class.

"""


def is_same_class(obj, a_class):
    """Check object-class.

    Args:
        obj: To check.
        a_class: The class.
    Returns:
        True or false
    """
    return type(obj) == a_class
