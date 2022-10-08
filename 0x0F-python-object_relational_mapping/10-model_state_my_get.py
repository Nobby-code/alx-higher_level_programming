#!/usr/bin/python3

"""
Script that prints the State object with the name passed as an argument:
    script takes 4 argument:
        mysql username, mysql password, db name, state name to search
    Use modele SQLAlchemy
    import State and Base from model_state
    The script should connect to a MySQL server runnig on localhost, port 3306
    Result must display states.id, Not found if no name found
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

    statement = session.query(State).filter(
            State.name == argv[4]).first()
    if statement:
        print("{:d}".format(statement.id))
    else:
        print("Not found")
    session.close()
