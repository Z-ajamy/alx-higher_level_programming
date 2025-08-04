#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        return (length, sentence[0])
    else:
        length = 0
        return (length, None)
