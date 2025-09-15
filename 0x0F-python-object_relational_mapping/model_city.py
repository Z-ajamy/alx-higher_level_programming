#!/usr/bin/python3
"""SQLAlchemy ORM model for representing cities within US states.

This module defines the City model class that represents individual cities
in the database. Each city belongs to a specific state through a foreign key
relationship, establishing the many-to-one side of the State-City relationship.

The model includes:
    - Primary key identifier for each city
    - City name with string constraints
    - Foreign key reference to the parent state
    - Bidirectional relationship with State objects

Dependencies:
    - SQLAlchemy ORM framework
    - model_state module (Base declarative base and State model)

Typical usage example:
    from model_city import City
    from model_state import State
    
    city = City(name="San Francisco", state_id=1)
    session.add(city)
    session.commit()
"""
from sqlalchemy import Column, INTEGER, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    """SQLAlchemy model representing a city within a US state.
    
    This class defines the database table structure for storing city information.
    Each city is associated with exactly one state through a foreign key relationship,
    forming the many-to-one side of the State-City relationship.
    
    Attributes:
        id (int): Primary key identifier for the city record. Auto-incrementing
            integer that uniquely identifies each city.
        name (str): The name of the city, limited to 128 characters maximum.
            Cannot be null as every city must have a name.
        state_id (int): Foreign key reference to the states table. Links this
            city to its parent state. Cannot be null as every city must belong
            to a state.
        state (relationship): SQLAlchemy relationship object that provides
            direct access to the associated State instance. Uses back_populates
            for bidirectional access.
    
    Database Table:
        Table name: 'cities'
        Foreign Keys: state_id references states.id
        Relationships: Many-to-one with 'states' table
        
    Example:
        # Create a city associated with state ID 5
        city = City(name="Los Angeles", state_id=5)
        
        # Access the state through the relationship
        print(city.state.name)  # Prints the state name
    """
    __tablename__ = 'cities'
    id = Column(INTEGER, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(INTEGER,
                    ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
