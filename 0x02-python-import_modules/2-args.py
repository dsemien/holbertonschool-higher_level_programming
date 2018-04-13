#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    pirate = len(argv) - 1
    index = 1
    if len(argv) == 1:
        print("{} arguments.".format(pirate))
    elif len(argv) == 2:
        print("{} argument:".format(pirate))
        print("{}: {}".format(index, argv[index]))
    else:
        print("{} arguments:".format(pirate))
        for index in range(1, len(argv)):
            print("{}: {}".format(index, argv[index]))
