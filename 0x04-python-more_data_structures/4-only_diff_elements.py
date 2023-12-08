#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set1 = set(set_1)
    set2 = set(set_2)

    unique_to_set1 = set1 - set2
    unique_to_set2 = set2 - set1

    return unique_to_set1, unique_to_set2


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}

    differentSentence = only_diff_elements(set_1, set_2)
    print(sorted(list(differentSentence)))
