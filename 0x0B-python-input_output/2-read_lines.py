#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='UTF-8') as f:
        for linecount, line in enumerate(f, 1):
            if nb_lines <= 0 or nb_lines >= linecount:
                print(line, end="")
