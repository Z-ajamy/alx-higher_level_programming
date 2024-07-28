-- The SHOW CREATE TABLE command provides the SQL statement that was used to create the specified table.
-- This command is useful to see the table's creation details, including its structure and any constraints.

-- Show the CREATE TABLE statement for the table named 'first_table'
SHOW CREATE TABLE `first_table`;

-- Explanation:
-- 1. SHOW CREATE TABLE: This command displays the SQL statement that was used to create the specified table.
-- 2. `first_table`: The name of the table for which to display the CREATE TABLE statement. The table name is enclosed in backticks to avoid conflicts with reserved keywords.

-- Usage:
-- This command is useful for understanding the structure of an existing table, including column definitions, data types, and constraints.
-- It is also helpful when you need to recreate a table with the same structure in another database or environment.

-- Example output:
-- The command returns a table with two columns: 'Table' and 'Create Table'.
-- Example:
-- +-------------+----------------------------------------------+
-- | Table       | Create Table                                 |
-- +-------------+----------------------------------------------+
-- | first_table | CREATE TABLE `first_table` (                 |
-- |             |   `id` INT,                                  |
-- |             |   `name` VARCHAR(256)                        |
-- |             | ) ENGINE=InnoDB DEFAULT CHARSET=utf8         |
-- +-------------+----------------------------------------------+
-- The 'Create Table' column contains the full CREATE TABLE statement used to create the table.
