#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [None] * len(my_list)
    i = len(my_list)
    for j in range(i):
        if my_list[j] % 2 == 0:
            new_list[j] = True
        else:
            new_list[j] = False
    return new_list
