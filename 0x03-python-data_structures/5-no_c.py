#!/usr/bin/python3
def no_c(my_string):
    letters_to_remove = "Cc"
    for letter in letters_to_remove:
        my_string = my_string.replace(letter, '') 
    return my_string
