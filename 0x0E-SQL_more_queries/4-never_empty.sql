-- Create a table named 'id_not_null' if it doesn't already exist
-- Note: Despite the table name suggesting 'id_not_null', there's no NOT NULL constraint on name
-- The id column has a default value but can still be NULL if explicitly set
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,       -- Integer column with default value of 1 (still allows NULL if explicitly set)
    name VARCHAR(256)       -- Variable-length string column (allows NULL, no constraints)
);
