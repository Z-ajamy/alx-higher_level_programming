#!/usr/bin/python3
"""MySQL Database Query Script for Cities with State Information.

This script connects to a MySQL database and retrieves city information
along with their corresponding state names using a JOIN operation.
It demonstrates relational database querying with proper connection 
handling and comprehensive error management.

The script returns city ID, city name, and state name for all cities
in the database by joining the cities and states tables.

Example:
    $ python3 script.py username password database_name

Requirements:
    - MySQLdb module (MySQL-python)
    - MySQL database server running on localhost:3306
    - Database with 'cities' and 'states' tables with proper foreign key relationship
    - Valid database credentials with SELECT permissions

Expected Output:
    Each row contains: (city_id, city_name, state_name)
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Main execution block for cities and states JOIN query operations.
    
    This script performs the following operations:
    1. Parses command-line arguments for database connection parameters
    2. Establishes connection to MySQL database on localhost:3306
    3. Executes JOIN query to retrieve cities with their state information
    4. Prints each row containing city ID, city name, and state name
    5. Ensures proper cleanup of database resources
    
    Command-line Arguments:
        sys.argv[1] (str): Database username
        sys.argv[2] (str): Database password
        sys.argv[3] (str): Database name
        
    Expected Database Schema:
        Table 'cities' with columns:
        - 'id': Primary key for city records
        - 'name': City name
        - 'state_id': Foreign key referencing states.id
        
        Table 'states' with columns:
        - 'id': Primary key for state records
        - 'name': State name
        
    JOIN Operation:
        Uses INNER JOIN to combine cities and states tables based on
        the foreign key relationship (cities.state_id = states.id).
        Returns only cities that have a corresponding state record.
    """
    # Store command-line arguments for database connection
    argv = sys.argv
    
    # Initialize connection and cursor variables for proper cleanup
    conn = None
    cursor = None

    try:
        # Establish MySQL database connection with explicit parameters
        conn = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3],port=3306)
        
        # Create cursor object for executing SQL queries
        cursor = conn.cursor()
        
        # Execute JOIN query to retrieve city information with state names
        # Selects city ID, city name, and corresponding state name
        # Uses INNER JOIN on foreign key relationship (cities.state_id = states.id)
        cursor.execute("SELECT cities.id, cities.name, states.name FROM" \
        " cities JOIN states ON cities.state_id = states.id ORDER BY cities.id")
        
        # Fetch all rows from the JOIN query result
        rows = cursor.fetchall()
        
        # Iterate through and print each row (city_id, city_name, state_name)
        for row in rows:
            print(row)
            
    except MySQLdb.Error as e:
        # Handle any MySQL-related errors and print error message
        print(e)
    finally:
        # Ensure proper cleanup of database resources
        # Close cursor if it was successfully created
        if cursor:
            cursor.close()
        # Close database connection if it was successfully established
        if conn:
            conn.close()
