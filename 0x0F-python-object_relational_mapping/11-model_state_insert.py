#!/usr/bin/python3

"""
Script that adds the State object "Louisaina" to the database hbtn_0e_6_usa:
    It takes 3 arguments:
        username, password, db name
    Use SQLAlchemy module
    import State and Base from model_state
    SQL server in he localhost at port 3306
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

    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)
    session.close()
