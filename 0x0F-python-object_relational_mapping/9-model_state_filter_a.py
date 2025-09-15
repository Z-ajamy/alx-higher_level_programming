#!/usr/bin/python3
"""SQLAlchemy ORM script to query states containing the letter 'a'.

This script connects to a MySQL database using SQLAlchemy ORM, creates the
necessary schema (if it does not already exist), and queries the `states`
table for all states whose names contain the letter 'a'. Results are then
printed to stdout in ascending order by ID.

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name>

Example:
    ./script_name.py root mypassword hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    # Create a database engine bound to the given MySQL database credentials.
    # The connection string uses the format:
    #   mysql+mysqldb://<username>:<password>@localhost/<database_name>
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            argv[1], argv[2], argv[3]
        )
    )

    # Ensure that all tables defined in the Base metadata exist in the database.
    Base.metadata.create_all(engine)

    # Create a configured "Session" class bound to the engine.
    Sess = sessionmaker(bind=engine)

    # Instantiate a session for interacting with the database.
    s = Sess()

    # Query all states whose name contains the letter 'a'.
    # The results are ordered by the state's ID in ascending order.
    rows = s.query(State).where(State.name.like('%a%')).order_by(State.id)

    # Close the session to free resources.
    s.close()

    # Print each state's ID and name to stdout in the specified format.
    for row in rows:
        print('{}: {}'.format(row.id, row.name))
