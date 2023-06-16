#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    list_1 = []
    list_2 = []

    for element in my_list:
        multiply_tuple = element[0] * element[1]
        list_1.append(multiply_tuple)
        list_2.append(element[1])

    result = sum(list_1) / sum(list_2)
    return result
