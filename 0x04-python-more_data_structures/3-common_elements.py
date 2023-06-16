#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    common_elts = set_1.intersection(set_2)
    new_set.update(common_elts)
    return new_set
