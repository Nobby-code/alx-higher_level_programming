#!/usr/bin/python3

"""
script that lists all states from hbtn_0e_0_usa database
script should take 3 arguments: username, password and database name

"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = conn.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id ASC')
    state = cur.fetchall()
    for s in state:
        print(s)
    cur.close()
    conn.close()
