#!/usr/bin/python3

'''
 Python script that takes in a URL, sends a request to the URL
 displays the body of the response (decoded in utf-8)

 You have to manage urllib.error.HTTPError exceptions and print:
    Error code: followed by the HTTP status code
'''
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            html = resp.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
