#!/usr/bin/python3
"""SQLAlchemy ORM Script for Querying the First State Record.

This script connects to a MySQL database using SQLAlchemy ORM and retrieves
the first state record from the 'states' table (ordered by ID), displaying
it in a formatted output. It demonstrates SQLAlchemy session management,
query operations, and the use of the first() method for single record retrieval.

The script creates database tables if they don't exist, queries for the first
state record by ID order using the first() method, and displays the state
with its ID and name.

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


if __name__ == '__main__':
    """Main execution block for first state record retrieval.
    
    This block performs the following operations:
    1. Creates database engine using command-line credentials
    2. Ensures database tables exist (creates if necessary)
    3. Creates and configures database session
    4. Queries for the first state record ordered by ID
    5. Closes session and displays the result
    
    The script uses SQLAlchemy's first() method which is more efficient
    than slicing for single record retrieval and returns None if no
    records exist (though this is not handled in this implementation).
    """

    # Create database engine using MySQL connector with command-line credentials
    # Connection string uses multi-line formatting for better readability
    # Format: mysql+mysqldb://username:password@host/database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        .format(argv[1], argv[2], argv[3]))

    # Create all database tables defined in the Base metadata
    # This will create the 'states' table if it doesn't already exist
    Base.metadata.create_all(engine)

    # Create sessionmaker class bound to the database engine
    # This factory will create database session instances for queries
    Sess = sessionmaker(bind=engine)
    
    # Create a new database session instance for executing queries
    s = Sess()

    # Query for the first State record ordered by ID using the first() method
    # first() is more efficient than [:1] slicing for single record retrieval
    # Returns the State object with the lowest ID, or None if no records exist
    row1 = s.query(State).order_by(State.id).first()
    
    # Close the database session to free up resources
    # Important to close sessions to prevent connection leaks
    s.close()

    # Print the formatted output showing ID and state name
    # Assumes row1 is not None (i.e., at least one state exists in the table)
    print('{}: {}'.format(row1.id, row1.name))
