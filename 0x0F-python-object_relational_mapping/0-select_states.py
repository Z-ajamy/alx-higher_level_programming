#!/usr/bin/python3
"""MySQL Database Query Script for States Table.

This script connects to a MySQL database and retrieves all records from
the 'states' table, ordered by ID. It demonstrates proper database connection
handling with comprehensive error management and resource cleanup.

The script accepts command-line arguments for database authentication and
prints each row from the states table to standard output.

Example:
    $ python3 script.py username password database_name

Requirements:
    - MySQLdb module (MySQL-python)
    - MySQL database server running on localhost:3306
    - Database with a 'states' table containing an 'id' column
    - Valid database credentials with SELECT permissions
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Main execution block for database query operations.

    This script performs the following operations:
    1. Parses command-line arguments for database connection parameters
    2. Establishes connection to MySQL database on localhost:3306
    3. Executes SELECT query to fetch all states ordered by ID
    4. Prints each row to standard output
    5. Ensures proper cleanup of database resources

    Command-line Arguments:
        sys.argv[1] (str): Database username
        sys.argv[2] (str): Database password
        sys.argv[3] (str): Database name
    Expected Database Schema:
        Table 'states' with at minimum an 'id' column for ordering.
    """
    # Initialize connection and cursor variables for proper cleanup
    conn = None
    cursor = None
    try:
        # Store command-line arguments for database connection
        argv = sys.argv
        # Establish MySQL database connection with explicit port specification

        conn = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                               db=argv[3], port=3306)

        # Create cursor object for executing SQL queries
        cursor = conn.cursor()

        # Execute SELECT query to retrieve all states ordered by ID
        cursor.execute('SELECT * FROM states ORDER BY id')

        # Fetch all rows from the query result
        rows = cursor.fetchall()

        # Iterate through and print each row from the result set
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
