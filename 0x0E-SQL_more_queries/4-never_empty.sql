-- Create a table named 'force_name' if it doesn't already exist
-- Note: Despite the table name suggesting 'force_name', there's no NOT NULL constraint on name
-- The id column has a default value but can still be NULL if explicitly set
CREATE TABLE IF NOT EXISTS force_name(
    id INT DEFAULT 1,       -- Integer column with default value of 1 (still allows NULL if explicitly set)
    name VARCHAR(256)       -- Variable-length string column (allows NULL, no constraints)
);
