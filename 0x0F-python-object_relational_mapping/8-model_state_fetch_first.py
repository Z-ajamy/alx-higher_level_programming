#!/usr/bin/python3
"""SQLAlchemy ORM Script for Querying the First State Record with Error Handling.

This script connects to a MySQL database using SQLAlchemy ORM and retrieves
the first state record from the 'states' table (ordered by ID), displaying
it in a formatted output. It includes proper error handling for cases where
no records exist in the table.

The script creates database tables if they don't exist, queries for the first
state record by ID order using the first() method, and displays the state
with its ID and name, or "Nothing" if no records are found.

Example:
    $ python3 script.py username password database_name
    Output (with data): 1: Alabama
    Output (empty table): Nothing

Requirements:
    - sqlalchemy package
    - mysqlclient or PyMySQL package for MySQL connectivity
    - model_state module containing Base and State class definitions
    - MySQL database server running on localhost
    - Valid database credentials with CREATE and SELECT permissions

Expected Output Format:
    - If records exist: "ID: StateName" where ID is the lowest primary key
    - If no records exist: "Nothing"
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    """Main execution block for first state record retrieval with error handling.
    
    This block performs the following operations:
    1. Creates database engine using command-line credentials
    2. Ensures database tables exist (creates if necessary)
    3. Creates and configures database session
    4. Queries for the first state record ordered by ID
    5. Closes session and displays appropriate result
    6. Handles empty table case by printing "Nothing"
    
    The script uses SQLAlchemy's first() method which returns the first
    matching record or None if no records exist. The conditional check
    ensures appropriate output for both scenarios.

    Error Handling:
        - If states table is empty: prints "Nothing"
        - If states exist: prints formatted "ID: StateName"
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Sess = sessionmaker(bind=engine)
    s = Sess()

    row1 = s.query(State).order_by(State.id).first()
    s.close()
    if row1:
        print('{}: {}'.format(row1.id, row1.name))
    else:
        print("Nothing")
