-- The SELECT statement is used to retrieve data from a table.
-- The WHERE clause filters the rows based on a specified condition.
-- The ORDER BY clause sorts the retrieved data based on one or more columns.

-- Retrieve the 'score' and 'name' columns from the 'second_table'
-- Filter the rows where the 'name' column is not an empty string
-- Order the results by the 'name' column in ascending order
SELECT score, name FROM second_table WHERE name != "" ORDER BY name;

-- Explanation:
-- 1. SELECT score, name: Specifies the columns to retrieve.
--    - score: The column representing the score.
--    - name: The column representing the name.
-- 2. FROM second_table: Specifies the table from which to retrieve the data.
-- 3. WHERE name != "": Adds a condition to filter the rows.
--    - Only the rows where the 'name' column is not an empty string will be included in the result set.
--    - The != operator checks for inequality, meaning it will exclude rows where 'name' is exactly an empty string.
-- 4. ORDER BY name: Sorts the retrieved rows by the 'name' column in ascending order (A to Z).
--    - By default, the ORDER BY clause sorts in ascending order. To sort in descending order, use 'ORDER BY name DESC'.

-- Usage:
-- This command is useful for retrieving specific columns from a table while filtering out rows that do not meet a certain condition and sorting the results.
-- It helps in data analysis by excluding rows with empty values in the 'name' column and presenting the results in a sorted manner.

-- Example output:
-- The command returns a result set with the 'score' and 'name' columns for rows where 'name' is not an empty string, ordered by 'name'.
-- Example:
-- +-------+--------+
-- | score | name   |
-- +-------+--------+
-- |     2 | Alex   |
-- |     8 | Bob    |
-- |    10 | John   |
-- |    12 | Steve  |
-- +-------+--------+
-- Each row represents a unique combination of score and name, excluding rows with an empty name, sorted by the name in ascending order.
