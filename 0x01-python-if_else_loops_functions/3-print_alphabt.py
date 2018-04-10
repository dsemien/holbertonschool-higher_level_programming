#!/usr/bin/python3
for a in range(97, 123):
    if a == ord('e') or a == ('q'):
        continue
    else:
        print('{:s}'.format(chr(a)), end="")
        