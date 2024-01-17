#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        plural_s = "s" if argc > 1 else ""
        print(f"{argc} argument{plural_s}:")
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"{i}: {arg}")
