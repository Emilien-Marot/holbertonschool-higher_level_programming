#!/usr/bin/python3
'''
I think you are out of line
'''


def text_indentation(text):
    '''
    alright, you made your point
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    new_line = True
    for char in text:
        if new_line and char == ' ':
            continue
        new_line = False
        print(char, end="")
        if char in ('.', '?', ':'):
            print("\n")
            new_line = True
