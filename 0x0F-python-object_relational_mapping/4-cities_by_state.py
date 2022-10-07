#!/usr/bin/python3

"""
Script that lists all cities from the database hbtn_0e_4_usa
The script takes 3 arguments:
    mysql username, mysql password, databse name
    runs on localhost port 3306
    results must be sorted in ascending order by cities.id
    use execute() once
    code should not be executed when imported
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
    query = 'SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC'
    cur.execute(query)
    cties = cur.fetchall()
    if cties:
        for city in cties:
            print(city)
        cur.close()
        conn.close()
