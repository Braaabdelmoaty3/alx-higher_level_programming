#!/usr/bin/python3
def add_integer(a, b=98):
    if type (a) not in [float, int]:
        raise TypeError("a must be an integer")
    elif type (b) not in [float, int]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a+ b
