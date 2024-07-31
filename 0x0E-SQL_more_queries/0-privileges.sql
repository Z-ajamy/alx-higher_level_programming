-- The SHOW GRANTS statement is used to display the privileges granted to a MySQL user.

-- Show the grants for the user 'user_0d_1' connecting from 'localhost'
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Explanation:
-- This command retrieves and displays all the privileges that have been granted to the user 'user_0d_1' connecting from 'localhost'.
-- It is useful for checking what permissions a specific user has within the MySQL database.

-- Usage:
-- This command helps in auditing and managing user privileges by providing a detailed list of permissions for a specific user.

-- Example output:
-- The command returns a list of grants for the specified user.
-- Example:
-- +-------------------------------------------------------------+
-- | Grants for user_0d_1@localhost                               |
-- +-------------------------------------------------------------+
-- | GRANT USAGE ON *.* TO 'user_0d_1'@'localhost'                |
-- | GRANT SELECT, INSERT ON `database_name`.* TO 'user_0d_1'@'localhost' |
-- +-------------------------------------------------------------+
-- Each row represents a grant, showing the specific privileges and the scope (database or table) they apply to.

-- Show the grants for the user 'user_0d_2' connecting from 'localhost'
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- Explanation:
-- This command retrieves and displays all the privileges that have been granted to the user 'user_0d_2' connecting from 'localhost'.
-- It is useful for checking what permissions a specific user has within the MySQL database.

-- Usage:
-- This command helps in auditing and managing user privileges by providing a detailed list of permissions for a specific user.

-- Example output:
-- The command returns a list of grants for the specified user.
-- Example:
-- +-------------------------------------------------------------+
-- | Grants for user_0d_2@localhost                               |
-- +-------------------------------------------------------------+
-- | GRANT USAGE ON *.* TO 'user_0d_2'@'localhost'                |
-- | GRANT SELECT, UPDATE ON `database_name`.* TO 'user_0d_2'@'localhost' |
-- +-------------------------------------------------------------+
-- Each row represents a grant, showing the specific privileges and the scope (database or table) they apply to.
