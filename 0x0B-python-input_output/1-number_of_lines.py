#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding='UTF-8') as f:
        linecount = 0
        for linecount, line in enumerate(f, 1):
            pass
        return linecount
