#!/usr/bin/python3

'''
Script that lists all states with a name starting with N from hbtn_0e_0_usa db
It takes 4 arguments username, passwd, database name, state name
The script is safe from injection
'''


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
    cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY %s\
            ORDER BY states.id ASC", (argv[4],))
    state = cur.fetchall()
    for s in state:
        print(s)
    cur.close()
    conn.close()

