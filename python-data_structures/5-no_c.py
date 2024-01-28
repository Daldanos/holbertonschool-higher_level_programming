#!/usr/bin/python3
def no_c(my_string):
    my_table = my_string.maketrans("", "", "Cc")
    noc = my_string.translate(my_table)
    return noc
