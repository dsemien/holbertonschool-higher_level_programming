#!/usr/bin/python3
def remove_char_at(str, n):

    string = ""
    delete = 0
    for letter in str:
        if delete != n:
            string += letter
        delete +=1
    return(string)
