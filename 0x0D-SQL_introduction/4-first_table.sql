-- The CREATE TABLE command creates a new table with the specified columns and data types.
-- This command ensures that a new table is created if it does not already exist.

-- Create a table named 'first_table' with two columns: 'id' and 'name'.
-- The IF NOT EXISTS clause prevents an error from occurring if the table already exists.
CREATE TABLE IF NOT EXISTS `first_table` (
    `id` INT,                    -- 'id' column to store integer values
    `name` VARCHAR(256)          -- 'name' column to store variable-length strings up to 256 characters
);

-- Explanation:
-- 1. CREATE TABLE: This part of the command initiates the creation of a new table.
-- 2. IF NOT EXISTS: This clause ensures that the command only creates the table if it does not already exist.
-- 3. first_table: The name of the table to be created.
-- 4. id INT: Defines a column named 'id' that stores integer values.
-- 5. name VARCHAR(256): Defines a column named 'name' that stores variable-length strings up to 256 characters.

-- Usage:
-- This command is useful for creating a table when initializing a database schema, ensuring that the table is only created once.
-- It prevents errors from occurring if the table already exists, making the script idempotent.

-- Example output:
-- If the table 'first_table' does not exist, it will be created, and the server will return a confirmation message.
-- If the table already exists, the server will not create a new one and will not return an error.
