#!/usr/bin/python3

"""
Script that changes the name of a State object from the database hbtn_0e_6_usa:
    Takes 3 arguments:
        mysql username, mysql password, database name
    Must use the module SQLAlchemy
    Must import State and Base from model_state
    It should connect to a MySQL server running on localhost, port 3306
    Changes the name of the State where id = 2 to New Mexico
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

    delete_state = session.query(State).filter(State.name.like('%a%'))
    
    for obj in delete_state:
        session.delete(obj)
    session.commit()
    session.close()
