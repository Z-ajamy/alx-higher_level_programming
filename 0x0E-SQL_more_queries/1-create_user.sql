-- Create a new MySQL user if it doesn't already exist
-- This statement will fail due to incorrect password syntax
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all possible privileges on all databases and tables to the new user
-- This gives the user complete administrative access to the MySQL server
-- WARNING: This creates a superuser with full system privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
