#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for x in my_list:
        print(x)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
try:
    for x in my_list:
        print(x, end="")
except IndexError:
    print("the number is out of list.")
