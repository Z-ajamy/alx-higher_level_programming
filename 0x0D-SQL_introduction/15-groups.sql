-- The SELECT statement is used to retrieve data from a table.
-- The COUNT() function counts the number of rows that match a specified condition.
-- The GROUP BY clause groups rows that have the same values in specified columns into aggregated data.
-- The ORDER BY clause sorts the retrieved data based on one or more columns.

-- Retrieve the 'score' column and the count of 'score' occurrences from the 'second_table'
-- Group the results by the 'score' column
-- Order the results by the count of 'score' in descending order
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

-- Explanation:
-- 1. SELECT score, COUNT(score) AS number: Specifies the columns to retrieve.
--    - score: The column to be grouped.
--    - COUNT(score): Counts the number of occurrences of 'score' for each group of 'score'.
--    - AS number: Aliases the result of COUNT(score) as 'number'.
-- 2. FROM second_table: Specifies the table from which to retrieve the data.
-- 3. GROUP BY score: Groups the rows by the 'score' column, aggregating the count of occurrences for each group.
-- 4. ORDER BY number DESC: Sorts the grouped rows by the count of occurrences in descending order. This means the groups with the highest count will appear first.

-- Usage:
-- This command is useful for summarizing data by counting occurrences of unique values in a column and sorting the results based on the count.
-- It helps in data analysis by showing the frequency of each unique value and highlighting the most common values.

-- Example output:
-- The command returns a result set with the 'score' column and the count of 'score' occurrences, sorted by the count in descending order.
-- Example:
-- +-------+--------+
-- | score | number |
-- +-------+--------+
-- |    10 |      2 |
-- |     3 |      1 |
-- |     8 |      1 |
-- |    14 |      1 |
-- +-------+--------+
-- Each row represents a unique score value and the count of occurrences for that score, with the counts sorted from highest to lowest.
