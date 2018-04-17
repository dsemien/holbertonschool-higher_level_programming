#!/usr/bin/env python3
def no_c(my_string):
    new = ""
    for letter in my_string:
        if letter is 'c' or letter is 'C':
            letter = ""
        new += letter
    return(new)
