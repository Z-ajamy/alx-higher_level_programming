#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    First_character = sentence[0]
    if length == 0:
        First_character = None
    tuple_a = (length, First_character)
    return(tuple_a)
