-- Retrieve name and score columns from 'second_table', sorted by score in descending order
-- This creates a leaderboard/ranking showing highest scores first
-- Only returns the specified columns, not the id column
SELECT score, name 
FROM second_table 
ORDER BY score DESC;
