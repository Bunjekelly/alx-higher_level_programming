#!/usr/bin/python3
def multiple_returns(sentence):
    first_value = len(sentence)
    if len(sentence) == 0:
        second_value = 'None'
    else:
        second_value = sentence[0]
    return first_value, second_value
