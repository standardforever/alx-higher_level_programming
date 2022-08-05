#!/usr/bin/python3
import json
"""Json to python """

def from_json_string(my_str):
    """"It returns an object(python data) represented by a json string"""
    return json.loads(my_str)
