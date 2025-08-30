-- Create a new table named 'second_table' if it doesn't already exist
-- Table structure: id (integer), name (string up to 256 chars), score (integer)
CREATE TABLE IF NOT EXISTS second_table(
    id INT,                -- Integer column for unique identifiers
    name VARCHAR(256),     -- Variable-length string for names (max 256 characters)
    score INT              -- Integer column for storing numeric scores
);

-- Insert sample data into second_table
-- Each INSERT adds one row with values in column order: id, name, score

-- Add record for John with score of 10
INSERT INTO second_table VALUES (1, "John", 10);

-- Add record for Alex with score of 3
INSERT INTO second_table VALUES (2, "Alex", 3);

-- Add record for Bob with score of 14 (highest score)
INSERT INTO second_table VALUES (3, "Bob", 14);

-- Add record for George with score of 8
INSERT INTO second_table VALUES (4, "George", 8);
