#!/usr/bin/python3
"""
It sends a reques to the url and display
the X-Requested-Id variable
"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        page = response.getheader('X-Request-Id')
        print(page)
