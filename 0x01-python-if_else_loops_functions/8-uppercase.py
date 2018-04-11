#!/usr/bin/python3
def uppercase(str):
    upper_letter = ""
    for letter in str:
        upper = ord(letter)
        if ord('a') <= upper <= ord('z'):
            upper -= 32
        upper_letter += chr(upper)
    print("{:s}".format(upper_letter))
