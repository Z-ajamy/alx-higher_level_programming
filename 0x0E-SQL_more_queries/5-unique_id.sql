-- Create a table named 'unique_id' if it doesn't already exist
-- The id column must be unique across all rows but can be NULL
-- Table allows multiple rows with NULL id values (NULL != NULL in SQL)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE,          -- Integer column with uniqueness constraint (allows NULL)
    name VARCHAR(256)       -- Variable-length string column (allows NULL, no constraints)
);
