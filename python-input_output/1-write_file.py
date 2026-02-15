#!/usr/bin/python3
'''
Docstring for python-input_output.0-read_file
'''


def write_file(filename="", text=""):
    '''
    Docstring for read_file
    :param filename: Description
    '''
    length = None
    with open(filename, "w", encoding="utf-8") as file:
        length = file.write(text)
    if not file.closed:
        file.close()
    return length
