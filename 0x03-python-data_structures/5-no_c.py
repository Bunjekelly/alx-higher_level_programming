#!/usr/bin/python3
def no_c(my_string):
    value = ""
    count = 0
    for element in my_string:
        if element != 'c' and element != 'C':
            value += element
            count += 1
    return value
