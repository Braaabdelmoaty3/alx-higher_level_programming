#!/usr/bin/python3
import importlib


def print_variable():
    value_of_variable = importlib.import_module('variable_load_5')
    print(value_of_variable.a)


if __name__ == "__main__":
    print_variable()
