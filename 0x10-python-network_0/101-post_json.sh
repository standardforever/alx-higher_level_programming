#!/bin/bash
# Curl that sends a post request with JSON file to a URL
curl -sX "POST" -H 'Content-Type: application/json' -d @$2 $1
