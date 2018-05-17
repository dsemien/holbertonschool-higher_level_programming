#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding='UTF-8') as f:
        for linecount, line in enumerate(f):
            pass    
        return linecount + 1
