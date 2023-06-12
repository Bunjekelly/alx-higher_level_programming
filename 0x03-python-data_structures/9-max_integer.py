#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return 'None'
    else:
        biggest = my_list[2]
        for element in my_list:
            if element > biggest:
                biggest = element
    return biggest
