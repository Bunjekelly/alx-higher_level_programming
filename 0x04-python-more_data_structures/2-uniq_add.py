#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    set_num = set()
    for element in my_list:
        if isinstance(element, int) and element not in set_num:
            sum += element
            set_num.add(element)
    return sum
