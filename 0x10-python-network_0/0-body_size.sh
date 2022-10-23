#!/bin/bash
# it sends a request to url and display the length
curl -si developersmindset.tech | grep Content-Length | tail -c 4
