#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0:
        return(None)
    number = my_list[0]
    for biggest in my_list:
        if biggest > number:
            number = biggest
    return(number)
