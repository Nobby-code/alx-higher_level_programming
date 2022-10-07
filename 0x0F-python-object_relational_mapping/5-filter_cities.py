#!/usr/bin/python3

"""
Script that takes in the name of state as an argument:
    then lists all cities of that state using hbtn_0e_4_usa db
    It takes 4 arguments:
        username, password, db name, state name
    import MySQLdb module
    script connects to MySQL server on the localhost on port 3306
    result sorted in ascending order using cities.id
    use execute() only once
    The code should not be executed when imported
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
    query = 'SELECT cities.name from cities JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name LIKE BINARY %s'
    cur.execute(query, (argv[4],))
    result = cur.fetchall()
    if result:
        for res in result:
            print(res)
        cur.close()
        conn.close()
