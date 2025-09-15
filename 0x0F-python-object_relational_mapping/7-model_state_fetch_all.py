#!/usr/bin/python3
"""SQLAlchemy ORM Script for Querying All States.

This script connects to a MySQL database using SQLAlchemy ORM and retrieves
all state records from the 'states' table, displaying them in a formatted
list ordered by ID. It demonstrates basic SQLAlchemy session management
and query operations.

The script creates database tables if they don't exist, queries all states
ordered by ID, and displays each state with its ID and name in a formatted output.

Example:
    $ python3 script.py username password database_name
    Output:
    1: California
    2: Arizona
    3: Texas

Requirements:
    - sqlalchemy package
    - mysqlclient or PyMySQL package for MySQL connectivity
    - model_state module containing Base and State class definitions
    - MySQL database server running on localhost
    - Valid database credentials with CREATE and SELECT permissions

Expected Output Format:
    Each line contains: "ID: StateName" where ID is the primary key
    and StateName is the state name string.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    # Create database engine using MySQL connector with command-line credentials
    # Connection string format: mysql+mysqldb://username:password@host/database
    # Uses string formatting to insert argv[1]=username, argv[2]=password, argv[3]=database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))

    # Create all database tables defined in the Base metadata
    # This will create the 'states' table if it doesn't already exist
    Base.metadata.create_all(engine)

    # Create sessionmaker class bound to the database engine
    # This factory will create database session instances
    Sess = sessionmaker(bind=engine)

    # Create a new database session instance for executing queries
    s = Sess()

    # Query all State records from the database ordered by their ID column
    # Uses SQLAlchemy ORM query syntax: session.query(Model).order_by(column).all()
    rows = s.query(State).order_by(State.id).all()

    # Close the database session to free up resources
    # Important to close sessions to prevent connection leaks
    s.close()

    # Iterate through query results and print formatted output
    # Each row is a State object with id and name attributes
    for row in rows:
        # Format output as "ID: StateName" using row object attributes
        print('{}: {}'.format(row.id, row.name))
