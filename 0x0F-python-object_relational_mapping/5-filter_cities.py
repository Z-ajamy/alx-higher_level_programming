#!/usr/bin/python3
"""MySQL Database Query Script for Cities in a Specific State with Input Validation.

This script connects to a MySQL database and retrieves city names from
a specific state using a JOIN operation with parameterized query for safety.
It includes input validation and displays results as a comma-separated list
on a single line, or prints an empty line if no results are found.

The script validates that exactly 5 command-line arguments are provided
before attempting database operations. If the argument count is incorrect
or no cities are found, it prints an empty line.

Example:
    $ python3 script.py username password database_name "California"
    Output: Los Angeles, San Francisco, San Diego
    
    $ python3 script.py username password database_name "NonexistentState"
    Output: (empty line)
    
    $ python3 script.py username password
    Output: (empty line)

Requirements:
    - MySQLdb module (MySQL-python)
    - MySQL database server running on localhost:3306
    - Database with 'cities' and 'states' tables with proper foreign key relationship
    - Valid database credentials with SELECT permissions

Expected Output:
    - City names separated by commas if cities are found
    - Empty line if no cities found or incorrect argument count
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Main execution block for state-specific city lookup with validation.
    
    This script performs the following operations:
    1. Validates command-line argument count (must be exactly 5)
    2. Parses command-line arguments for database connection and state name
    3. Establishes connection to MySQL database on localhost:3306
    4. Executes parameterized JOIN query to find cities in specified state
    5. Handles empty result sets gracefully
    6. Formats output as comma-separated list or empty line
    7. Ensures proper cleanup of database resources
    
    Command-line Arguments (must provide exactly 5):
        sys.argv[0] (str): Script name (automatic)
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
        
    Output Behavior:
        - Prints comma-separated city names if cities found in specified state
        - Prints empty line if no cities found in the state
        - Prints empty line if incorrect number of arguments provided
    """
    # Store command-line arguments for validation and database operations
    argv = sys.argv
    
    # Initialize connection and cursor variables for proper cleanup
    conn = None
    cursor = None

    # Validate that exactly 5 command-line arguments are provided
    # (script name + 4 required parameters)
    if len(argv) == 5:
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

            # Get total number of cities found
            l = len(rows)
            
            # Handle case where no cities are found in the specified state
            if l == 0:
                # Print empty line when no results found
                print()
            else:
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
    else:
        # Print empty line if incorrect number of arguments provided
        # Expected: script_name username password database_name state_name (5 total)
        print()
