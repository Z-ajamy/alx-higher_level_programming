#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        First_character = None
    else:
        First_character = sentence[0]
    tuple_a = (length, First_character)
    return (tuple_a)
