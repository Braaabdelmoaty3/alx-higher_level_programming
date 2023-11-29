#!/usr/bin/python3

i = 'a'

while True:
    print(i, end='')
    i = chr(ord(i) + 1)

    if i > 'z':
        break
