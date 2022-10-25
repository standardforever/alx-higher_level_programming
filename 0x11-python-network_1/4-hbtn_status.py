#!/usr/bin/python3
"""
It fetches url
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        page = response.read().decode('utf-8')
        print("Body response:")
        print("    - type: {}".format(type(page)))
        print("    - content: {}".format(page))
