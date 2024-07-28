-- The SELECT statement is used to retrieve data from a table.
-- The asterisk (*) is a wildcard character that means "all columns."

-- Retrieve all records from the table named 'first_table'
SELECT * FROM `first_table`;

-- Explanation:
-- 1. SELECT *: This part of the command selects all columns from the specified table.
-- 2. FROM `first_table`: Specifies the table from which to retrieve the data. The table name is enclosed in backticks to avoid conflicts with reserved keywords.

-- Usage:
-- This command is useful for retrieving all the data from a table, which can be helpful for viewing the entire contents of the table.

-- Example output:
-- The command returns a result set with all rows and columns from the table 'first_table'.
-- Example:
-- +----+---------------------------+
-- | id | name                      |
-- +----+---------------------------+
-- |  1 | Alice                     |
-- |  2 | Bob                       |
-- |  3 | Charlie                   |
-- +----+---------------------------+
-- Each row represents a record in the table, and each column corresponds to the fields defined in the table.
