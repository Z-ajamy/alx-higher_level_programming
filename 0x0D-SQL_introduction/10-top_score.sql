-- The SELECT statement is used to retrieve specific columns from a table.
-- The ORDER BY clause sorts the retrieved data based on one or more columns.

-- Retrieve the 'score' and 'name' columns from the table named 'second_table'
-- Sort the results by the 'score' column in ascending order
SELECT `score`, `name` FROM `second_table` ORDER BY `score` ASC;

-- Explanation:
-- 1. SELECT `score`, `name`: This part of the command specifies the columns to retrieve from the table.
-- 2. FROM `second_table`: Specifies the table from which to retrieve the data. The table name is enclosed in backticks to avoid conflicts with reserved keywords.
-- 3. ORDER BY `score`: Adds a clause to sort the retrieved rows based on the 'score' column.
-- 4. ASC: Specifies that the sorting should be in ascending order. ASC is the default sorting order, but it is explicitly stated here for clarity.

-- Usage:
-- This command is useful for retrieving specific columns from a table and sorting the results based on one or more columns.
-- Sorting in ascending order means that the lowest scores will appear first.

-- Example output:
-- The command returns a result set with the 'score' and 'name' columns sorted by 'score' in ascending order.
-- Example:
-- +-------+--------+
-- | score | name   |
-- +-------+--------+
-- |     3 | Alex   |
-- |     8 | George |
-- |    10 | John   |
-- |    14 | Bob    |
-- +-------+--------+
-- Each row represents a record in the table, with the scores sorted from lowest to highest.
