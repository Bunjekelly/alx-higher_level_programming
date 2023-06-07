#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            alpha = chr(ord(c)-32)
        else:
            alpha = c
        print("{}".format(alpha), end="")
    print()
