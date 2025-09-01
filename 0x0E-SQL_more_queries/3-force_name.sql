-- Create a table named 'force_name' if it doesn't already exist
-- This table enforces that names must be provided (cannot be NULL)
-- Table structure designed for storing entities that require valid names
CREATE TABLE IF NOT EXISTS force_name(
    id INT,                    -- Integer column for identifiers (allows NULL, no constraints)
    name VARCHAR(256) NOT NULL -- Variable-length string column, NULL values prohibited
);
