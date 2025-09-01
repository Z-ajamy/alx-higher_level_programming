-- Create a table named 'unique_id' if it doesn't already exist
-- The id column has both a default value and uniqueness constraint
-- This ensures all id values are unique across the table
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,  -- Integer column: defaults to 1, must be unique across all rows
    name VARCHAR(256)         -- Variable-length string column (allows NULL, no constraints)
);
