#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    add = 0
    for number in range(1, len(argv)):
        add += int(argv[number])
    print("{}".format(add))
