#!/usr/bin/python3

'''
Script that takes in a letter and sends a post request to:
    http://0.0.0.0:5000/search_user with the letter as a parameter
The letter must be sent in the variable q
If no argument given, set q=''
If te response is properly JSON formatted and not empty, display:
    the id and name like [<id>] <name>
Otherwise display:
    Not a valid JSON if he JSON is invalid
    No result if the JSON is empty
Use he packages requests and sys
'''

import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        data = r.json()
        if data:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
