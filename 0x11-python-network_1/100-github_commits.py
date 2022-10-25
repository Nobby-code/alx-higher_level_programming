#!/usr/bin/python3

'''
listing 10 commits from the most recent to oldest
'''

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'
    r = requests.get(url.format(sys.argv[2], sys.argv[1]))
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
