#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Return a set of elements present in only one set."""
    set1 = set(set_1)
    set2 = set(set_2)

    only_diff_elements_set = set1.symmetric_difference(set2)

    return only_diff_elements_set


if __name__ == "__main__":
    # Example sets
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}

    # Get elements present in only one set
    result_set = only_diff_elements(set_1, set_2)

    # Display the result
    print(sorted(list(result_set)))
