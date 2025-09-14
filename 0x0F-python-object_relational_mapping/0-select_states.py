#!/usr/bin/python3
"""
MySQL Database Connection and Query Utility Script.

This module provides utility functions for connecting to a MySQL database
and executing queries. It includes functions for creating connections,
executing queries that modify data, and fetching query results.

The script accepts command-line arguments for database connection parameters
and demonstrates basic database operations by fetching all records from
a 'states' table.

Example:
    $ python3 script.py username password database_name

Attributes:
    DB_cfg (dict): Database configuration dictionary containing connection
        parameters parsed from command-line arguments.

Requirements:
    - MySQLdb module (MySQL-python)
    - MySQL database server
    - Appropriate database permissions for the specified user
"""

import MySQLdb
import sys

# Database configuration dictionary built from command-line arguments
# Expected format: python script.py <username> <password> <database_name>
DB_cfg = {'host':'localhost', 'user':sys.argv[1], 'passwd': sys.argv[2], 'db': sys.argv[3]}

def create_con(DB_cfg):
    """Create and return a MySQL database connection.
    
    Establishes a connection to a MySQL database using the provided
    configuration parameters. Handles connection errors gracefully.
    
    Args:
        DB_cfg (dict): Dictionary containing database connection parameters.
            Expected keys: 'host', 'user', 'passwd', 'db'.
    
    Returns:
        MySQLdb.Connection: Active database connection object if successful.
        
    Raises:
        MySQLdb.Error: If connection to database fails.
        
    Note:
        The function will print the error and exit if connection fails.
    """
    try:
        conn = MySQLdb.connect(**DB_cfg)
        return conn
    except MySQLdb.Error as e:
        print(e)
        exit


def do_exe_query(conn, query, args=None):
    """Execute a query that modifies data (INSERT, UPDATE, DELETE).
    
    Executes a database query that changes data and commits the transaction.
    Includes proper error handling with rollback functionality and ensures
    the cursor is always closed.
    
    Args:
        conn (MySQLdb.Connection): Active database connection object.
        query (str): SQL query string to execute.
        args (tuple, optional): Parameters to be passed to the query.
            Defaults to None.
    
    Raises:
        MySQLdb.Error: If query execution fails. Error is printed and
            transaction is rolled back.
            
    Note:
        This function automatically commits successful transactions and
        rolls back failed ones.
    """
    c = conn.cursor()
    try:
        c.execute(query, args)
        conn.commit()
    except MySQLdb.Error as e:
        conn.rollback()
        print(e)
    finally:
        c.close()



def do_fetch_query(conn, query, args=None):
    """Execute a SELECT query and return all results.
    
    Executes a database query that retrieves data and returns all matching
    rows. Includes proper error handling and ensures the cursor is always
    closed.
    
    Args:
        conn (MySQLdb.Connection): Active database connection object.
        query (str): SQL SELECT query string to execute.
        args (tuple, optional): Parameters to be passed to the query.
            Defaults to None.
    
    Returns:
        tuple: All rows returned by the query as a tuple of tuples,
            or None if an error occurred.
            
    Raises:
        MySQLdb.Error: If query execution fails. Error is printed and
            None is returned.
    """
    res = None
    c = conn.cursor()
    try:
        c.execute(query, args)
        res = c.fetchall()
        return res
    except MySQLdb.Error as e:
        print(e)
        return None
    finally:
        c.close()

if __name__ == '__main__':
    """Main execution block.
    
    Demonstrates basic database operations by:
    1. Creating a database connection using command-line arguments
    2. Executing a SELECT query to fetch all states ordered by ID
    3. Printing each result row
    4. Properly closing the connection when done
    
    The script expects exactly 3 command-line arguments:
    - sys.argv[1]: database username
    - sys.argv[2]: database password  
    - sys.argv[3]: database name
    """
    try:
        conn = create_con(DB_cfg)
        celect_all = "SELECT * FROM states ORDER BY id"
        res = do_fetch_query(conn, celect_all)
        if res != None:
            for i in res:
                print(i)
    finally:
        conn.close()
