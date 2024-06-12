#!/usr/bin/python3
def new_in_list(my_list, idx, element):
# 1- my file take a copy from it 
# 2- replace the no. with his index without do any thing in the orginal list 
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    my_list[idx] = element
    return new_list
