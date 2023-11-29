#!/usr/bin/python3
i = 'a'
while True:
    print(i,end='')
    i = chr(ord(i) + 1)
# (chr) connvert the unicode to character 
# (ord) convert the charater in the variable into unicode 
    if i > 'z':
        break
