#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary.keys())
    for i in sort:
        print("{}: {}".format(i, a_dictionary[i]))
