-- Attempt to select cities from all states named 'California'
-- CORRECTED: Use IN for subquery matching
-- CORRECTED: Added quotes around string literal
SELECT id, name 
FROM cities 
WHERE state_id IN (                    
    SELECT id 
    FROM states 
    WHERE name = 'California'          
);
