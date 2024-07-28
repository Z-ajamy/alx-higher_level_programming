-- The UPDATE statement is used to modify existing records in a table.
-- The SET clause specifies the columns to be updated and their new values.
-- The WHERE clause filters the rows that should be updated based on a specified condition.

-- Update the 'score' column to 10 for the record in the 'second_table' where the 'name' is "Bob"
UPDATE `second_table` SET `score` = 10 WHERE `name` = "Bob";

-- Explanation:
-- 1. UPDATE `second_table`: Specifies the table in which the records should be updated. The table name is enclosed in backticks to avoid conflicts with reserved keywords.
-- 2. SET `score` = 10: Specifies the column to be updated and the new value to be assigned to it. In this case, the 'score' column is set to 10.
-- 3. WHERE `name` = "Bob": Adds a condition to filter the rows that should be updated. Only the rows where the 'name' is "Bob" will be updated.

-- Usage:
-- This command is useful for modifying existing records in a table based on specific conditions.
-- It allows for updating one or more columns for the filtered rows.

-- Example:
-- Before the update:
-- +----+--------+-------+
-- | id | name   | score |
-- +----+--------+-------+
-- |  1 | John   |    10 |
-- |  2 | Alex   |     3 |
-- |  3 | Bob    |    14 |
-- |  4 | George |     8 |
-- +----+--------+-------+

-- After the update:
-- +----+--------+-------+
-- | id | name   | score |
-- +----+--------+-------+
-- |  1 | John   |    10 |
-- |  2 | Alex   |     3 |
-- |  3 | Bob    |    10 |
-- |  4 | George |     8 |
-- +----+--------+-------+
-- The 'score' for the record where 'name' is "Bob" has been updated to 10.
