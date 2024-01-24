#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    format_string = "\n".join("{} ".format(item) for item in my_list)
    return format_string


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    fornmat_string = print_reversed_list_integer(my_list)
    print(fornmat_string)
