#!/usr/bin/python3
"""Database query script for displaying cities with their associated states.

This module connects to a MySQL database and retrieves all cities along with
their corresponding state information. The cities are displayed in a formatted
output showing the state name, city ID, and city name, ordered by city ID.

The script expects three command-line arguments:
    - Database username
    - Database password  
    - Database name

Example:
    $ python3 script.py username password database_name

Dependencies:
    - SQLAlchemy ORM framework
    - MySQL database with mysqldb driver
    - Custom model classes (model_state.Base, model_state.State, model_city.City)

Typical usage example:
    $ python3 cities_by_state.py root password hbtn_0e_14_usa
"""


from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from sys import argv

if __name__ == "__main__":
    """Main execution block for the database query script.
    
    Creates a database connection using command-line arguments, establishes
    a session, queries all cities with their associated states using eager
    loading, and prints the results in a formatted manner.
    
    Command-line Args:
        argv[1] (str): MySQL username for database connection
        argv[2] (str): MySQL password for database connection  
        argv[3] (str): MySQL database name to connect to
        
    Output Format:
        Each line displays: "State Name: (City ID) City Name"
        Results are ordered by City ID in ascending order.
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    )

    Base.metadata.create_all(engine)

    sess = sessionmaker(bind=engine)

    with sess() as s:
        """Query all cities with their associated state information.
        
        Uses joinedload to eagerly fetch the related State objects to avoid
        N+1 query problems. Results are ordered by city ID for consistent output.
        """
        rows = s.query(City).options(joinedload(City.state)).order_by(City.id).all()

        for row in rows:
            """Print each city with its state information in the required format."""
            print("{}: ({}) {}".format(row.state.name, row.id, row.name))
