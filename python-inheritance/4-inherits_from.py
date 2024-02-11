#!/usr/bin/python3
"""

Checks if inherits from subclass.

"""


def inherits_from(obj, a_class):
    """return isinstance of obj"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
