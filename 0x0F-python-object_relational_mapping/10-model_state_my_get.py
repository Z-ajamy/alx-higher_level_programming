#!/usr/bin/python3
"""SQLAlchemy ORM script to query a state by name.

This script connects to a MySQL database using SQLAlchemy ORM, creates the
necessary schema (if it does not already exist), and queries the `states`
table for the first state whose name matches the provided argument.
The state's ID is then printed to stdout.

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name> <state_name>

Example:
    ./script_name.py root mypassword hbtn_0e_6_usa "Texas"
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

    # Query for the first state whose name matches the provided argument (argv[4]).
    # `.first()` ensures that only one result (the first match) is retrieved.
    row1 = s.query(State).where(State.name == '{}'.format(argv[4])).first()

    # Close the session to free resources.
    s.close()

    # Print the ID of the matched state. Assumes that a result exists.
    print('{}'.format(row1.id))
