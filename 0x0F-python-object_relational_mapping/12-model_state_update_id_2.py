"""SQLAlchemy ORM script to update the name of a state.

This script connects to a MySQL database using SQLAlchemy ORM, creates the
necessary schema (if it does not already exist), and updates the name of the
state with ID = 2 to "New Mexico". The update is committed to the database
only if the state exists.

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
    # The connection string uses the format:
    #   mysql+mysqldb://<username>:<password>@localhost/<database_name>
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    )

    # Ensure that all tables defined in the Base metadata exist in the database.
    Base.metadata.create_all(engine)

    # Create a configured "Session" class bound to the engine.
    sess = sessionmaker(bind=engine)

    # Use a context manager to handle session lifecycle automatically.
    with sess() as s:
        # Retrieve the state with ID = 2 from the database.
        obj = s.query(State).filter_by(id=2).first()

        # If the state exists, update its name and commit the transaction.
        if obj:
            obj.name = 'New Mexico'
            s.commit()
