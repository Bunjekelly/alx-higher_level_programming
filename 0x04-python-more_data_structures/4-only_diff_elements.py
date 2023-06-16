#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    diff_elts = set_1 ^ set_2
    new_set.update(diff_elts)
    return new_set
