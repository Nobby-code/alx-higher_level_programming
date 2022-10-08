#!/usr/bin/python3

"""
Script that lists State objects from the database hbtn_0e_6_usa:
    Has 3 arguments:
        mysql username, password, database name
    Uses module SQLAlchemy
    Imports State and Base from model_state
    Connects to mysql server on localhost at port 3306
    Result sorted in ascending order by states.id
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # create a configures "Session" class
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    for state in session.query(State):
        print("{:d}: {:s}".format(state.id, state.name))
    session.close()
