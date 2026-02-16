#!/usr/bin/env python3
def serialize_and_save_to_file(data, filename):
    '''
    Docstring for serialize_and_save_to_file

    :param data: Description
    :param filename: Description
    '''
    import json
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)
    if not file.closed:
        file.close()


def load_and_deserialize(filename):
    '''
    Docstring for load_and_deserialize

    :param filename: Description
    '''
    import json
    res = None
    with open(filename, "r", encoding="utf-8") as file:
        res = json.load(file)
    if not file.closed:
        file.close()
    return res
