-- Calculate the average score from all records in second_table
-- Returns a single decimal value representing the mean of all score values
-- NULL values in the score column are automatically excluded from the calculation
SELECT AVG(score) AS `average` FROM second_table;
