#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    format_string = "\n".join("{} ".format(item) for item in my_list)
    return format_string

