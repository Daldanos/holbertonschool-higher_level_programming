#!/usr/bin/python3
"""

JSON writing

"""

import json


def load_from_json_file(filename):
    """write to a file"""
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)
    return data
