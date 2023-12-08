#!/usr/bin/python3
def common_elements(set_1, set_2):
    set1 = set(set_1)
    set2 = set(set_2)

    return set1 & set2


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
