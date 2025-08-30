-- Delete all records from second_table where the score is 5 or lower
-- This permanently removes rows that don't meet the minimum score threshold
-- WARNING: This is a destructive operation and cannot be easily undone
DELETE FROM second_table 
WHERE score <= 5;        -- Remove rows where score is less than or equal to 5
