#!/usr/bin/python3
"""

JSON writing

"""

import json


def save_to_json_file(my_obj, filename):
    """write to a file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
