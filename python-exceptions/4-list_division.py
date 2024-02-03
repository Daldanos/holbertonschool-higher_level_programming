#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            if (isinstance(my_list_1[i], (int, float)) and 
            isinstance(my_list_2[i], (int, float))):
                divid = my_list_1[i] / my_list_2[i]
                result.append(divid)
            else:
                print("wrong type")
                result.append(0)
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except IndexError:
            result.append(0)
            print("out of range")
    return result
