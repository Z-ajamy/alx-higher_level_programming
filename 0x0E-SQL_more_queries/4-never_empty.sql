-- Create a table named 'id_not_null' if it doesn't already exist
-- Note: Despite the table name suggesting 'not null', the id column can still be NULL
-- The DEFAULT 1 clause provides a fallback value when no id is specified
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,      -- Integer column with default value of 1 (still allows NULL)
    name VARCHAR(256)      -- Variable-length string column (allows NULL, no default)
);
