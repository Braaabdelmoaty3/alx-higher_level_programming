#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list


if __name__ == '__main__':
    my_list = [1, 2, 3, 4]
    idx = 2
    element = 10
    new_list = replace_in_list(my_list, idx, element)

    print(new_list)
    print(my_list)
