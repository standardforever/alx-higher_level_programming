#!/bin/bash
# Curl display all HTTP methods the server will accept
curl -IsLX OPTIONS $1 | grep allow | cut -d ":" -f2- | cut -d " " -f2-
