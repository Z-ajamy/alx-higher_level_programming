-- Count how many students have each score value (frequency distribution)
-- Groups records by score and counts occurrences of each score
-- SYNTAX ERRORS: 'orded' should be 'ORDER', 'escd' should be 'ASC' or 'DESC'
-- This query will fail due to spelling mistakes in the ORDER BY clause
SELECT 
    score,                    -- The score value
    COUNT(score) AS number    -- Count of how many records have this score
FROM second_table 
GROUP BY score               -- Group rows by score value to enable counting
ORDER BY score DESC;          -- CORRECTED: Sort results by score in ascending order
