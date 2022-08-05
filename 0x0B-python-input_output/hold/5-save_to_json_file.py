#!/usr/bin/python3

import json
""""define from _json file"""

def save_to_json_file(my_obj, filename):
    """"it write an Object to a text file, using Json representation"""
    with open(filename, 'w') as f:
        obj = json.dumps(my_obj)
        f.write(obj)
