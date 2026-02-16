#!/usr/bin/python3
'''
Docstring for python-input_output.0-read_file
'''


def class_to_json(obj):
    '''
    Docstring for read_file
    :param filename: Description
    '''
    import json
    return json.dumps(obj.__dict__)
