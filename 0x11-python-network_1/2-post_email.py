#!/usr/bin/python3

'''POST request with email as a parameter'''
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    params = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(params).encode("UTF-8")
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as resp:
        html = resp.read()
        print(html.decode('UTF-8'))
