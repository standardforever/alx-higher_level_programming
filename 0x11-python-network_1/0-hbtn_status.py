#!/usr/bin/python3

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    data = response.read()
    print("Body response:")
    print("    - type:", type(data))
    print("    - content:", data)
    print("    - utf8 content:", data.decode("utf-8"))
