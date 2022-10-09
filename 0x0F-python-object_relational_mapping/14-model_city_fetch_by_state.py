#!/usr/bin/python3

"""
Script that prints all city objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    join_query = session.query(State, City).join(City).all()

    for state, city in join_query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
