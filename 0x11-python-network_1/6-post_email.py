#!/usr/bin/python3
"""
Sends a POST request to the passed URL
"""
import sys
import requests


if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], email)
    print(response.text)
