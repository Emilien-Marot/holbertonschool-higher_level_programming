#!/usr/bin/python3
'''
Docstring for python-input_output.7-add_item
'''
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    list_json = load_from_json_file("add_item.json")
except:
    list_json = []
for i in range(1,len(sys.argv)):
    list_json.append(sys.argv[i])
save_to_json_file(list_json, "add_item.json")