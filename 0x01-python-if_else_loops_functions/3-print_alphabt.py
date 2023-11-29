#!/usr/bin/python3
i = 'a'
for i in range(97,123):
    if i != ord('q') and i != ord('e'):
        print("{}".format(chr(i)),end="")

# Loop through ASCII values for lowercase letters (97 to 122)
#or i in range(97, 123):
#    # Use one print function with string format to print characters without a new line, excluding 'q' and 'e'
#    print("{}".format(chr(i)), end='') if chr(i) not in ['q', 'e'] else None
