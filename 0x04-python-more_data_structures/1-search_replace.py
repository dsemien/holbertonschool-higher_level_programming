#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return[replace if digit is search else digit for digit in my_list]
