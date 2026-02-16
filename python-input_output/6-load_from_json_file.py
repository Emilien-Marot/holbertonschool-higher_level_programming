#!/usr/bin/python3
'''
Docstring for python-input_output.0-read_file
'''


def load_from_json_file(filename):
    '''
    Docstring for read_file
    :param filename: Description
    '''
    import json
    res = None
    with open(filename, "r", encoding="utf-8") as file:
        res = json.load(file)
    if not file.closed:
        file.close()
    return res
