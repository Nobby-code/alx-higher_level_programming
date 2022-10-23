#!/usr/bin/python3

'''
Python script that takes in a URL and an email address
    Sends a POST request to the passed URL with the email as aparameter
    And finally displays the body of the response
The email must be sent in the variable email
You must use the packages: requets and sys
'''

import requests
import sys

if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    url = sys.argv[1]
    r = requests.post(url, data=values)
    print(r.text)
