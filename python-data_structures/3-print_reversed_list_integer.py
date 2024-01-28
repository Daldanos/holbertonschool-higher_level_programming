#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list)

    for j in reversed(range(i)):
        print("{}".format(my_list[j]))
