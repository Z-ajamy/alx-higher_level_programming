-- Retrieve score and name for records where score is 10 or higher
-- Results are sorted from highest to lowest score (descending order)
-- This filters out low-performing records and creates a "qualifying scores" list
SELECT score, name 
FROM second_table 
WHERE score >= 10        -- Filter: only include scores of 10 or above
ORDER BY score DESC;     -- Sort: highest scores appear first
