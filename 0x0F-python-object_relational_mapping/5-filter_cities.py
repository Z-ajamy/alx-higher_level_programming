#!/usr/bin/python3
"""MySQL Database Query Script for Cities in a Specific State.

This script connects to a MySQL database and retrieves city names from
a specific state using a JOIN operation with parameterized query for safety.
It displays the results as a comma-separated list on a single line.

The script accepts a state name as the fourth command-line argument and
returns all city names in that state, ordered by city ID, formatted as
a comma-separated list.

Example:
    $ python3 script.py username password database_name "California"
    Output: Los Angeles, San Francisco, San Diego

Requirements:
    - MySQLdb module (MySQL-python)
    - MySQL database server running on localhost:3306
    - Database with 'cities' and 'states' tables with proper foreign key relationship
    - Valid database credentials with SELECT permissions

Expected Output:
    City names separated by commas, with the last city name having no trailing comma.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Main execution block for state-specific city lookup operations.
    
    This script performs the following operations:
    1. Parses command-line arguments for database connection and state name
    2. Establishes connection to MySQL database on localhost:3306
    3. Executes parameterized JOIN query to find cities in specified state
    4. Formats output as comma-separated list on single line
    5. Ensures proper cleanup of database resources
    
    Command-line Arguments:
        sys.argv[1] (str): Database username
        sys.argv[2] (str): Database password
        sys.argv[3] (str): Database name
        sys.argv[4] (str): State name to filter cities by
        
    Expected Database Schema:
        Table 'cities' with columns:
        - 'id': Primary key for city records (used for ordering)
        - 'name': City name
        - 'state_id': Foreign key referencing states.id
        
        Table 'states' with columns:
        - 'id': Primary key for state records
        - 'name': State name (used for filtering)
        
    Query Details:
        Uses parameterized query (%s) for safe SQL execution and prevention
        of SQL injection attacks. Results are ordered by city ID.
        
    Output Formatting:
        Cities are printed as comma-separated values on a single line,
        with no trailing comma after the last city name.
    """
    # Store command-line arguments for database connection and state filter
    argv = sys.argv
    
    # Initialize connection and cursor variables for proper cleanup
    conn = None
    cursor = None

    try:
        # Establish MySQL database connection with explicit parameters
        conn = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3],port=3306)
        
        # Create cursor object for executing SQL queries
        cursor = conn.cursor()
        
        # Execute parameterized JOIN query to get cities in specified state
        # Uses line continuation with backslash for query readability
        # Parameterized query (%s) prevents SQL injection attacks
        cursor.execute("SELECT cities.name FROM" \
        " cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id", (argv[4],))
        
        # Fetch all city names matching the specified state
        rows = cursor.fetchall()

        # Get total number of cities for comma formatting logic
        l = len(rows)
        
        # Iterate through cities and format as comma-separated list
        for i in range(l):
            # Check if this is the last city in the list
            if i == l - 1:
                # Print last city name without trailing comma and with newline
                print(rows[i][0])
            else:
                # Print city name followed by comma and space (no newline)
                print(rows[i][0], end=', ')
                
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
