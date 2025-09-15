#!/usr/bin/python3
"""SQLAlchemy ORM Model Definition for States Table.

This module defines a SQLAlchemy ORM model for the 'states' table using
declarative base pattern. It provides object-relational mapping capabilities
for database operations on state records.

The State model includes basic state information with proper column constraints
and data types, following SQLAlchemy best practices for model definition.

Example Usage:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    
    # Create engine and session
    engine = create_engine('mysql://user:pass@localhost/dbname')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create a new state
    new_state = State(name='California')
    session.add(new_state)
    session.commit()
    
    # Query states
    states = session.query(State).all()

Requirements:
    - sqlalchemy package
    - Compatible database driver (e.g., PyMySQL, mysqlclient)

Database Schema:
    The State model maps to a 'states' table with the following structure:
    - id: Primary key integer column (auto-incrementing)
    - name: State name string column (max 128 characters, required)
"""

from sqlalchemy import create_engine, Column, INTEGER, String
from sqlalchemy.orm import declarative_base

# Create declarative base class for ORM model definitions
# All ORM model classes will inherit from this base
Base = declarative_base()


class State(Base):
    """SQLAlchemy ORM model for the states table.
    
    This class defines the structure and constraints for state records
    in the database. It uses SQLAlchemy's declarative base pattern to
    map Python class attributes to database table columns.
    
    Attributes:
        __tablename__ (str): Database table name ('states')
        id (Column): Primary key integer column for unique state identification
        name (Column): State name string column with 128 character limit
        
    Table Structure:
        CREATE TABLE states (
            id INTEGER PRIMARY KEY NOT NULL,
            name VARCHAR(128) NOT NULL
        );
        
    Column Details:
        - id: Integer primary key, auto-incrementing, cannot be null
        - name: Variable character string up to 128 characters, cannot be null
        
    Usage Examples:
        # Create a new state instance
        state = State(name='Texas')
        
        # Access state attributes
        print(state.id)    # Primary key (set after database insert)
        print(state.name)  # State name string
    """
    # Specify the database table name that this model maps to
    __tablename__ = 'states'
    
    # Define primary key column: auto-incrementing integer ID
    # Column parameters: name, data type, primary key flag, nullable constraint
    id = Column('id', INTEGER, primary_key=True, nullable=False)
    
    # Define state name column: string with maximum length of 128 characters
    # Column parameters: name, data type with length constraint, nullable constraint
    name = Column('name', String(128), nullable=False)
