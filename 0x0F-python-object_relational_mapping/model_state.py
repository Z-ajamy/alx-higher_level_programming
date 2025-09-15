#!/usr/bin/python3
"""SQLAlchemy ORM model for representing US states.

This module defines the State model class using SQLAlchemy's declarative base
approach. The State model represents individual US states in the database and
establishes a one-to-many relationship with cities.

The model includes:
    - Primary key identifier
    - State name with string constraints
    - Bidirectional relationship with City objects
    - Cascade deletion for associated cities

Dependencies:
    - SQLAlchemy ORM framework
    - Related City model (circular import relationship)

Typical usage example:
    from model_state import Base, State
    from sqlalchemy import create_engine
    
    engine = create_engine('sqlite:///example.db')
    Base.metadata.create_all(engine)
"""
from sqlalchemy import Column, INTEGER, String
from sqlalchemy.orm import declarative_base, relationship 

Base = declarative_base()


class State(Base):
    """SQLAlchemy model representing a US state.
    
    This class defines the database table structure and relationships for
    storing US state information. Each state can have multiple associated
    cities through a one-to-many relationship.
    
    Attributes:
        id (int): Primary key identifier for the state record.
        name (str): The name of the state, limited to 128 characters.
        cities (relationship): Collection of City objects associated with this state.
            Supports bidirectional access and automatic cascade deletion.
    
    Database Table:
        Table name: 'states'
        Relationships: One-to-many with 'cities' table
        
    Example:
        state = State(name="California")
        session.add(state)
        session.commit()
    """
    __tablename__ = 'states'
    id = Column('id', INTEGER, primary_key=True, nullable=False)
    
    name = Column('name', String(128), nullable=False)

    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
