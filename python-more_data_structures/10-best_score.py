#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_key = None
    for key in a_dictionary.keys():
        if max_key is None or a_dictionary[key] > a_dictionary[max_key]:
            max_key = key
    return max_key
