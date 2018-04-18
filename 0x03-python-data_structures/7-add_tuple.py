#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        tuple_a += (0,0)
        tuple_b += (0,0)
    if len(tuple_a) > 2 or len(tuple_b) > 2:
        tuple_a = tuple_a[:2]
        tuple_b = tuple_b[:2]

    tu_1 = tuple_a[0] + tuple_b[0]
    tu_2 = tuple_a[1] + tuple_b[1]
    new = (tu_1, tu_2)
    return(new)
