#!/usr/bin/python3
reverse = ""
for alpha in range(122, 96, -1):
    if alpha % 2 == 0:
        reverse += chr(alpha)
    else:
        reverse += chr(alpha - 32)
print("{}".format(reverse), end="")
