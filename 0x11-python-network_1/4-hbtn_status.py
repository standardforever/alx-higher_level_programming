#!/usr/bin/python3
"""
It fetches url
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req =  requests.get(url)
    print("Body response:")
    print("    - type: {}".format(type(req.text)))
    print("    - content: {}".format(req.text))
