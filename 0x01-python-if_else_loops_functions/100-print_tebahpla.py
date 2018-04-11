#!/usr/bin/python3
for number in range(122, 96, -1):
    letter = number
    alphabet = ""
    if letter % 2 != 0:
        letter -= 32
        alphabet += chr(letter)
    else:
        alphabet += chr(letter)
    print("{:s}".format(alphabet), end="")
