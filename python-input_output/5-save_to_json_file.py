#!/usr/bin/python3
'''
Docstring for python-input_output.0-read_file
'''


def save_to_json_file(my_obj, filename):
    '''
    Docstring for read_file
    :param filename: Description
    '''
    import json
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
    if not file.closed:
        file.close()
