-- The SELECT statement is used to retrieve specific columns from a table.
-- The WHERE clause filters the rows based on a specified condition.
-- The ORDER BY clause sorts the retrieved data based on one or more columns.

-- Retrieve the 'score' and 'name' columns from the table named 'second_table'
-- Filter the results to include only rows where the 'score' is greater than or equal to 10
-- Sort the results by the 'score' column in descending order
SELECT `score`, `name` FROM `second_table` 
WHERE `score` >= 10 
ORDER BY `score` DESC;

-- Explanation:
-- 1. SELECT `score`, `name`: Specifies the columns to retrieve from the table.
-- 2. FROM `second_table`: Specifies the table from which to retrieve the data. The table name is enclosed in backticks to avoid conflicts with reserved keywords.
-- 3. WHERE `score` >= 10: Adds a condition to filter the rows to include only those where the 'score' is greater than or equal to 10.
-- 4. ORDER BY `score` DESC: Adds a clause to sort the filtered rows based on the 'score' column in descending order. This means the highest scores will appear first.

-- Usage:
-- This command is useful for retrieving specific columns from a table, filtering the results based on a condition, and sorting the filtered results.
-- Sorting in descending order means that the highest scores will appear first.

-- Example output:
-- The command returns a result set with the 'score' and 'name' columns filtered by the specified condition and sorted by 'score' in descending order.
-- Example:
-- +-------+--------+
-- | score | name   |
-- +-------+--------+
-- |    14 | Bob    |
-- |    10 | John   |
-- +-------+--------+
-- Each row represents a record in the table that meets the condition, with the scores sorted from highest to lowest.
