#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    string = []
    for number in my_list:
        if number % 2 is 0:
            string.append(True)
        else:
            string.append(False)
    return(string)
