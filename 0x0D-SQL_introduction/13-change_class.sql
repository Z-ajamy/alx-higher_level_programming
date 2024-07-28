-- The DELETE statement is used to remove existing records from a table.
-- The WHERE clause specifies the condition that determines which rows should be deleted.

-- Delete records from the 'second_table' where the 'score' column is less than or equal to 5
DELETE FROM `second_table` WHERE `score` <= 5;

-- Explanation:
-- 1. DELETE FROM `second_table`: Specifies the table from which records should be deleted. The table name is enclosed in backticks to avoid conflicts with reserved keywords.
-- 2. WHERE `score` <= 5: Adds a condition to filter the rows that should be deleted. Only the rows where the 'score' is less than or equal to 5 will be deleted.

-- Usage:
-- This command is useful for removing specific records from a table based on a condition.
-- It helps in cleaning up data by removing unwanted or obsolete records.

-- Example:
-- Before the delete:
-- +----+--------+-------+
-- | id | name   | score |
-- +----+--------+-------+
-- |  1 | John   |    10 |
-- |  2 | Alex   |     3 |
-- |  3 | Bob    |    10 |
-- |  4 | George |     8 |
-- +----+--------+-------+

-- After the delete:
-- +----+--------+-------+
-- | id | name   | score |
-- +----+--------+-------+
-- |  1 | John   |    10 |
-- |  3 | Bob    |    10 |
-- |  4 | George |     8 |
-- +----+--------+-------+
-- The record where 'score' is 3 has been deleted.
