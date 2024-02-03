#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0

    for j in my_list:
        try:
            print("{:d}".format(j), end="")
            i += 1
        except (ValueError, TypeError):
            pass
        if i == x:
            break
    print()
    return i
