#!/usr/bin/python3

def append_write(filename="", text=""):
    """it append a string at the end of a file"""
    with open(filename, 'a', encoding='UTF8') as f:
        return f.write(text)