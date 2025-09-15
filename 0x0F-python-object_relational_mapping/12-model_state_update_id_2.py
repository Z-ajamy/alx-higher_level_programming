#!/usr/bin/python3
"""SQLAlchemy ORM script to update a state's name in the database.

This script connects to a MySQL database using SQLAlchemy ORM, ensures that
the schema exists, and updates the name of the state with ID = 2 to
"New Mexico". If the state with ID = 2 exists, the change is committed to
the database.

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name>

Example:
    ./script_name.py root mypassword hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Create a database engine bound to the given MySQL database credentials.
    # Connection string format:
    #   mysql+mysqldb://<username>:<password>@localhost/<database_name>
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    )

    # Ensure that all tables defined in Base.metadata exist in the database.
    Base.metadata.create_all(engine)

    # Create a configured "Session" class bound to the engine.
    sess = sessionmaker(bind=engine)

    # Use context manager to handle session lifecycle (open/close).
    with sess() as s:
        # Query for the state with ID = 2.
        obj = s.query(State).filter_by(id=2).first()

        # If the state exists, update its name and commit the transaction.
        if obj:
            obj.name = 'New Mexico'
            s.commit()

