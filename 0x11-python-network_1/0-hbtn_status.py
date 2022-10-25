#!/usr/bin/python3
"""
Prints different results of
a request
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        data = response.read()
        print("Body response:")
        print("    - type:", type(data))
        print("    - content:", data)
        print("    - utf8 content:", data.decode("utf-8"))
