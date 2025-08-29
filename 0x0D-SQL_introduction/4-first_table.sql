-- Create a table named 'first_table' if it doesn't already exist
-- The IF NOT EXISTS clause prevents errors if the table is already present
-- Table structure:
--   - id: Integer column (no constraints specified)
--   - name: Variable character string up to 256 characters
CREATE TABLE IF NOT EXISTS first_table(
    id INT,                -- Integer column for storing numeric identifiers
    name VARCHAR(256)      -- Variable-length string column (max 256 characters)
);
