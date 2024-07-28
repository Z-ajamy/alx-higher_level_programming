-- The SELECT statement is used to retrieve data from a table.
-- The WHERE clause filters the rows based on a specified condition.

-- Retrieve the 'score' and 'name' columns from the 'second_table'
-- Filter the rows where the 'name' column is not an empty string
SELECT score, name FROM second_table WHERE name != "";

-- Explanation:
-- 1. SELECT score, name: Specifies the columns to retrieve.
--    - score: The column representing the score.
--    - name: The column representing the name.
-- 2. FROM second_table: Specifies the table from which to retrieve the data.
-- 3. WHERE name != "": Adds a condition to filter the rows.
--    - Only the rows where the 'name' column is not an empty string will be included in the result set.
--    - The != operator checks for inequality, meaning it will exclude rows where 'name' is exactly an empty string.

-- Usage:
-- This command is useful for retrieving specific columns from a table while filtering out rows that do not meet a certain condition.
-- It helps in data analysis by excluding rows with empty values in the 'name' column, ensuring that only rows with meaningful 'name' values are included.

-- Example output:
-- The command returns a result set with the 'score' and 'name' columns for rows where 'name' is not an empty string.
-- Example:
-- +-------+--------+
-- | score | name   |
-- +-------+--------+
-- |    10 | John   |
-- |     3 | Alex   |
-- |    10 | Bob    |
-- |     8 | George |
-- +-------+--------+
-- Each row represents a unique combination of score and name, excluding rows with an empty name.
