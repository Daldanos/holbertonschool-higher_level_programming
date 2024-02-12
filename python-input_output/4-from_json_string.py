#!/usr/bin/python3
"""

JSON representation of an object

"""

import json


def from_json_string(my_str):
    """function to return a JSON of an object"""
    return json.loads(my_str)
