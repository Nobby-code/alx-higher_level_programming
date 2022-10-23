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
    '''
    name = str(sys.argv[1])
    pswd = str(sys.argv[2])
    url = 'https://api.github.com/users/{}'.format(name)
    r = requests.get(url, auth=HTTPBasicAuth(name, pswd))
    print(r.json().get('id'))
    '''
    user = str(sys.argv[1])
    pw = str(sys.argv[2])
    result = requests.get("https://api.github.com/user",
                          auth=(HTTPBasicAuth(user, pw)))

    try:
        data = result.json()
        print(data["id"])
    except Exception:
        print("None")
