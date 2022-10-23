#!/usr/bin/python3

'''script that takes in a url, send a request to the url and displays 
the value of X-Request-Id variable found on he header'''
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        print(resp.headers['X-Request-Id'])
