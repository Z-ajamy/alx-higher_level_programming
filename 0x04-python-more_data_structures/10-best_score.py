#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        greater_val = 0
        greater_key = ""
        for key, val in a_dictionary.items():
            if val > greater_val:
                greater_val = val
                greater_key = key
        return greater_key
