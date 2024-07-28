-- The INSERT INTO command is used to add new records to a table.
-- This command specifies the columns to be inserted and the corresponding values.

-- Insert a new record into the table named 'first_table'
INSERT INTO `first_table` (`id`, `name`) 
VALUES (89, "Best School");

-- Explanation:
-- 1. INSERT INTO `first_table`: This part of the command specifies the table into which the new record will be inserted. The table name is enclosed in backticks to avoid conflicts with reserved keywords.
-- 2. (`id`, `name`): Specifies the columns that will receive the new values. These column names are enclosed in backticks.
-- 3. VALUES: Introduces the list of values to be inserted.
-- 4. (89, "Best School"): Provides the values for the specified columns. The value 89 is inserted into the 'id' column, and the string "Best School" is inserted into the 'name' column.

-- Usage:
-- This command is useful for adding a new record to the specified table, with values corresponding to the specified columns.

-- Example output:
-- After executing this command, the table 'first_table' will have a new record with 'id' = 89 and 'name' = "Best School".
-- Example:
-- +----+-------------+
-- | id | name        |
-- +----+-------------+
-- | 89 | Best School |
-- +----+-------------+
