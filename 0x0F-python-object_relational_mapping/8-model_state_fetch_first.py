#!/usr/bin/python3
"""SQLAlchemy ORM Script for Querying the First State Record.

This script connects to a MySQL database using SQLAlchemy ORM and retrieves
the first state record from the 'states' table (ordered by ID), displaying
it in a formatted output. It demonstrates SQLAlchemy session management,
query operations, and result limiting.

The script creates database tables if they don't exist, queries for the first
state record by ID order, and displays the state with its ID and name.

Example:
    $ python3 script.py username password database_name
    Output:
    1: Alabama

Requirements:
    - sqlalchemy package
    - mysqlclient or PyMySQL package for MySQL connectivity
    - model_state module containing Base and State class definitions
    - MySQL database server running on localhost
    - Valid database credentials with CREATE and SELECT permissions
    - At least one record in the 'states' table

Expected Output Format:
    Single line containing: "ID: StateName" where ID is the lowest primary key
    and StateName is the corresponding state name string.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

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

# Query for the first State record ordered by ID using slice notation
# Uses SQLAlchemy ORM query with ordering and limiting: query().order_by().[:1]
# The [:1] slice limits the result to only the first record
rows = s.query(State).order_by(State.id)[:1]

# Close the database session to free up resources
# Important to close sessions to prevent connection leaks
s.close()

# Iterate through query results (will be only one record) and print formatted output
# Even though we expect only one result, we use a loop for consistency with SQLAlchemy patterns
for row in rows:
    # Format output as "ID: StateName" using row object attributes
    # This will display the state with the lowest ID value
    print('{}: {}'.format(row.id, row.name))
