-- The SELECT statement is used to retrieve data from a table.
-- The SUM() function calculates the sum of a specified column's values.
-- The GROUP BY clause groups rows that have the same values in specified columns into aggregated data.

-- Retrieve the 'score' column and the sum of 'score' values grouped by 'score' from the 'second_table'
SELECT `score`, SUM(`score`) AS `number` FROM `second_table` GROUP BY `score`;

-- Explanation:
-- 1. SELECT `score`, SUM(`score`) AS `number`: This part of the command specifies the columns to retrieve.
--    - `score`: The column to be grouped.
--    - SUM(`score`): Calculates the sum of 'score' values for each group of 'score'.
--    - AS `number`: Aliases the result of SUM(`score`) as `number`.
-- 2. FROM `second_table`: Specifies the table from which to retrieve the data. The table name is enclosed in backticks to avoid conflicts with reserved keywords.
-- 3. GROUP BY `score`: Groups the rows by the 'score' column, aggregating the sum of 'score' values for each group.

-- Usage:
-- This command is useful for aggregating data based on unique values in a column and performing calculations, such as summing values within each group.
-- It helps in data analysis by summarizing the data according to the specified grouping criteria.

-- Example output:
-- The command returns a result set with the 'score' column and the sum of 'score' values grouped by 'score'.
-- Example:
-- +-------+--------+
-- | score | number |
-- +-------+--------+
-- |     3 |      3 |
-- |     8 |      8 |
-- |    10 |     20 |
-- |    14 |     14 |
-- +-------+--------+
-- Each row represents a unique score value and the sum of scores for that group.
