#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = ""
    if idx < 0:
        return(my_list)
    elif idx >= len(my_list):
        return(my_list)
    else:
        new = my_list[:]
        new[idx] = element
        return(new)
