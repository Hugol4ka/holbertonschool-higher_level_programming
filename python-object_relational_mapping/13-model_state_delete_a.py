#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()
