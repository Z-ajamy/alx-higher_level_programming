-- The CREATE TABLE command creates a new table with the specified columns and data types.
-- This command ensures that a new table is created if it does not already exist.

-- Create a table named 'second_table' with three columns: 'id', 'name', and 'score'.
-- The IF NOT EXISTS clause prevents an error from occurring if the table already exists.
CREATE TABLE IF NOT EXISTS `second_table` (
    id INT,                    -- 'id' column to store integer values
    name VARCHAR(256),         -- 'name' column to store variable-length strings up to 256 characters
    score INT                  -- 'score' column to store integer values
);

-- Explanation:
-- 1. CREATE TABLE: Initiates the creation of a new table.
-- 2. IF NOT EXISTS: Ensures the command only creates the table if it does not already exist.
-- 3. `second_table`: The name of the table to be created.
-- 4. id INT: Defines a column named 'id' that stores integer values.
-- 5. name VARCHAR(256): Defines a column named 'name' that stores variable-length strings up to 256 characters.
-- 6. score INT: Defines a column named 'score' that stores integer values.

-- Usage:
-- This command is useful for creating a table when initializing a database schema, ensuring that the table is only created once.
-- It prevents errors from occurring if the table already exists, making the script idempotent.

-- Example output:
-- If the table 'second_table' does not exist, it will be created, and the server will return a confirmation message.
-- If the table already exists, the server will not create a new one and will not return an error.

-- Insert records into the 'second_table'
-- The INSERT INTO command is used to add new records to a table.
-- This command specifies the columns to be inserted and the corresponding values.

INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
-- Inserts a record with 'id' = 1, 'name' = "John", and 'score' = 10 into the 'second_table'

INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
-- Inserts a record with 'id' = 2, 'name' = "Alex", and 'score' = 3 into the 'second_table'

INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
-- Inserts a record with 'id' = 3, 'name' = "Bob", and 'score' = 14 into the 'second_table'

INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
-- Inserts a record with 'id' = 4, 'name' = "George", and 'score' = 8 into the 'second_table'

-- Explanation:
-- 1. INSERT INTO `second_table`: Specifies the table into which the new record will be inserted. The table name is enclosed in backticks to avoid conflicts with reserved keywords.
-- 2. (`id`, `name`, `score`): Specifies the columns that will receive the new values. These column names are enclosed in backticks.
-- 3. VALUES: Introduces the list of values to be inserted.
-- 4. (1, "John", 10): Provides the values for the specified columns for the first record.
-- 5. (2, "Alex", 3): Provides the values for the specified columns for the second record.
-- 6. (3, "Bob", 14): Provides the values for the specified columns for the third record.
-- 7. (4, "George", 8): Provides the values for the specified columns for the fourth record.

-- Usage:
-- These commands are used to add new records to the specified table, with values corresponding to the specified columns.
-- This is essential for populating the table with data.

-- Example output:
-- After executing these commands, the table 'second_table' will have the following records:
-- +----+--------+-------+
-- | id | name   | score |
-- +----+--------+-------+
-- |  1 | John   |    10 |
-- |  2 | Alex   |     3 |
-- |  3 | Bob    |    14 |
-- |  4 | George |     8 |
-- +----+--------+-------+
-- Each row represents a record in the table, and each column corresponds to the fields defined in the table.
