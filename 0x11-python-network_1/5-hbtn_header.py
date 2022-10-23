#!/usr/bin/python3

'''
Python script that takes in URL, sends request o the URL,
    then displays X-Request-Id variable in the response header
Use requests package
Import sys
'''

import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])

    print(r.headers.get('X-Request-Id'))
