#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set(my_list)
    total_sum = sum(unique_numbers)
    return total_sum


if __name__ == "__main__":
    # Example usage:
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    result = uniq_add(my_list)
    print(result)
