#!/usr/bin/python3

'''
Python script that takes your GITHUB credentials: username and password
    And uses GITHUB API to display your id
First argument will be your name
Second argument will be your password (access token)
Use the packages: requests and sys
'''

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    name = sys.argv[1]
    pswd = sys.argv[2]
    url = 'https://api.github.com/users/{}'.format(name)
    r = requests.get(url, auth=HTTPBasicAuth(name, pswd))
    print(r.json().get('id'))
