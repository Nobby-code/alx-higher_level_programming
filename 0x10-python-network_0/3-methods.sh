#!/bin/bash
# Script that takes in a URL and displays all HTTP methods that server will accept
curl -sI "$1" | grep "Allow: " | sed 's/Allow: //'
