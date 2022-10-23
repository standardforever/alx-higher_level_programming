#!/bin/bash
# it sends a request to url and display the length
curl -si $1 | grep Content-Length | tail -c 4
