#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    suma = 0

    for i in range(x):
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                suma += 1
        except (ValueError, TypeError):
            pass
    print()
    return suma
