#!/usr/bin/python3
"""SQLAlchemy ORM script to insert a new state into the database.

This script connects to a MySQL database using SQLAlchemy ORM, creates the
necessary schema (if it does not already exist), and inserts a new state
named "Louisiana" into the `states` table. The script then prints the ID of
the newly inserted state.

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
    s = None
    try:
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

        # Create a new State object with the name "Louisiana".
        obj = State(name='Louisiana')

        # Add the new state object to the session.
        s.add(obj)

        # Commit the transaction so that the new state is saved to the database.
        s.commit()

        # Print the ID of the newly created state object.
        print(obj.id)

    finally:
        # Ensure the session is closed to free resources,
        # even if an error occurs during execution.
        if s:
            s.close()
