#!/bin/bash
# curl that causes a server to respond with a message
curl -sX PUT -L -d "user_id=98" -H 'origin: ALX' 0.0.0.0:5000/catch_me
