#!/usr/bin/python3
def read_file(filename=""):
    """It reads a text file and print to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        file = f.read()
        print("{}".format(file))
