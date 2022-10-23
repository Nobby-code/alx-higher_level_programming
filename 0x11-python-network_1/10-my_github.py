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

    name= str(sys.argv[1])
    pswd = str(sys.argv[2])
    r = requests.get("https://api.github.com/user",
                          auth=(HTTPBasicAuth(name, pswd)))

    try:
        data = r.json()
        print(data["id"])
    except Exception:
        print("None")
