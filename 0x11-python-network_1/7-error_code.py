#!/usr/bin/python3
"""
it handle request error
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    try:
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(response.status_code))
