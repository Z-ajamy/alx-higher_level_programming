-- The CREATE TABLE statement is used to create a new table in a database.
-- The IF NOT EXISTS clause ensures that the table is only created if it does not already exist.

-- Create the table 'id_not_null' if it does not already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,          -- Column 'id' of type INT (integer) with a default value of 1
    name VARCHAR(256)          -- Column 'name' of type VARCHAR with a maximum length of 256 characters
);

-- Explanation:
-- 1. CREATE TABLE IF NOT EXISTS: Creates a new table only if it does not already exist.
-- 2. id_not_null: Specifies the name of the table to be created.
-- 3. id INT DEFAULT 1: Defines a column named 'id' with the data type INT.
--    - DEFAULT 1: Specifies a default value of 1 for the 'id' column. If no value is provided during insertion, the column will default to 1.
-- 4. name VARCHAR(256): Defines a column named 'name' with the data type VARCHAR, allowing up to 256 characters.
--    - This column can store variable-length character strings but does not have a default value or NOT NULL constraint.

-- Usage:
-- This command is useful for creating a table where the 'id' column will automatically default to 1 if no value is provided,
-- and the 'name' column can store up to 256 characters without any default value or NOT NULL constraint.

-- Example:
-- The resulting table will have two columns:
-- - 'id': An integer column that defaults to 1 if no value is provided during insertion.
-- - 'name': A variable character column with a maximum length of 256 characters, which can be NULL.
