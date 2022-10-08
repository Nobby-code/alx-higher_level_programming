#!/usr/bin/python3

"""
Deleting all state objects with a name containing letter a
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
