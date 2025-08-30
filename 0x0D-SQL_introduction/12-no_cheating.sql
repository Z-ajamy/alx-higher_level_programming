-- Update Bob's score to 10 in the second_table
-- This modifies existing data rather than inserting new records
-- Uses WHERE clause to target only the specific record for "Bob"
UPDATE second_table 
SET score = 10           -- Change the score value to 10
WHERE name = "Bob";      -- Only update rows where name equals "Bob"
