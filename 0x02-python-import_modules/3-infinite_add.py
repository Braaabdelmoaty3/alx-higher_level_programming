#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    total = 0
    for arg in sys.argv[1:]:
        try:
            num_arg = int(arg)
            total += num_arg
        except ValueError:
            print(f"invalid argument :{arg}")
print(total)
