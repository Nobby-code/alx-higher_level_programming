#!/usr/bin/python3

'''POST request with email as a parameter'''
import urllib.request
import sys


if __name__ == "__main__":
    url = argv[1]
    params = {'email': argv[2]}
    data = urllib.parse.urlencode( params ).encode('UTF-8')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(url, data) as resp:
        html = resp.read()
        print(html.decode('UTF-8'))
