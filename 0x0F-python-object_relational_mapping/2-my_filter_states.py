#!/usr/bin/python3
"""MySQL Database Query Script for Specific State Lookup.

This script connects to a MySQL database and retrieves records from the
'states' table where the state name exactly matches a provided search term.
It uses string formatting to construct the SQL query and demonstrates 
database connection handling with comprehensive error management.

The script accepts a state name as the fourth command-line argument and
returns all matching records ordered by ID.

Example:
    $ python3 script.py username password database_name California
    $ python3 script.py username password database_name Texas

Requirements:
    - MySQLdb module (MySQL-python)
    - MySQL database server running on localhost:3306
    - Database with a 'states' table containing 'id' and 'name' columns
    - Valid database credentials with SELECT permissions

Security Note:
    This script uses string formatting to construct SQL queries. For production
    use, parameterized queries are recommended to prevent SQL injection attacks.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Main execution block for state name lookup operations.
    
    This script performs the following operations:
    1. Parses command-line arguments for database connection and search term
    2. Establishes connection to MySQL database on localhost:3306
    3. Executes SELECT query using string formatting for state name match
    4. Orders results by ID and prints each matching row
    5. Ensures proper cleanup of database resources
    
    Command-line Arguments:
        sys.argv[1] (str): Database username
        sys.argv[2] (str): Database password
        sys.argv[3] (str): Database name
        sys.argv[4] (str): State name to search for (exact match)
        
    Expected Database Schema:
        Table 'states' with columns:
        - 'id': Primary key or sortable identifier
        - 'name': State name column for exact matching
        
    Query Construction:
        Uses .format() method to insert the state name directly into the
        SQL query string within double quotes for exact string matching.
    """
    # Initialize connection and cursor variables for proper cleanup
    conn = None
    cursor = None
    try:
        # Store command-line arguments for database connection and search term
        argv = sys.argv
        
        # Establish MySQL database connection with explicit port specification
        conn = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
        
        # Create cursor object for executing SQL queries
        cursor = conn.cursor()
        
        # Execute SELECT query using string formatting to insert state name
        # The .format() method replaces {} with argv[4] within double quotes
        cursor.execute('SELECT * FROM states WHERE name = BINARY "{}" ORDER BY id'.format(argv[4]))

        # Fetch all rows matching the specified state name
        rows = cursor.fetchall()
        
        # Iterate through and print each matching row from the result set
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
