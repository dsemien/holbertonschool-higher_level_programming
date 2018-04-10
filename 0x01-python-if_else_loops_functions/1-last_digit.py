#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = str(number)[-1]
string = "Last digit of {:d} is and is {}".format(number, last_digit)

if int(last_digit) > 5:
    print("{} and is greater than {}".format(string, 5))
elif number == 0:
    print("{} and is {}".format(string, 0))
elif int(last_digit) < 6:
    print("{} and is less than {:d} and not {:d}".format(string, 6, 0))
