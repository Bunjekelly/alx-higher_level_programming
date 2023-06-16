#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_value = []
    for key, k in a_dictionary.items():
        if k == value:
            delete_value.append(key)
    for key in delete_value:
        del a_dictionary[key]
    return a_dictionary
