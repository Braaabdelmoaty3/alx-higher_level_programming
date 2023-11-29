#!/usr/bin/python3
i = 'a'
for i in range(97,123):
    if chr(i) not in ['q','e']:
        print("{}".format(chr(i)),end="")
#for i in range(97, 123):
#    if chr(i) not in ['a', 'b']:
#        print(chr(i), end='')
