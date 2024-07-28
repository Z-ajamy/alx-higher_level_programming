-- The SHOW TABLES command lists all the tables in the currently selected database.
-- This command is useful to get an overview of the tables present in the database.

-- List all tables in the currently selected database
SHOW TABLES;

-- Explanation:
-- 1. SHOW TABLES: This command displays a list of all tables in the current database.
-- 2. No parameters are required. The command operates on the database that is currently in use.

-- Usage:
-- Before running this command, ensure that you have selected the appropriate database using the USE command.
-- For example: USE `hbtn_0c_0`;

-- Example output:
-- The command returns a table with a single column containing the names of the tables.
-- Example:
-- +-----------------+
-- | Tables_in_db    |
-- +-----------------+
-- | Students        |
-- | Courses         |
-- | Enrollments     |
-- +-----------------+
-- Each row represents a table name in the current database.
