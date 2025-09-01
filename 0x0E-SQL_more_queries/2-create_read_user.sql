-- Create a new database named 'hbtn_0d_2' if it doesn't already exist
-- The IF NOT EXISTS clause prevents errors if the database is already present
-- Safe for running multiple times or in automated scripts
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create a new MySQL user if it doesn't already exist
-- User can only connect from localhost with the specified password
-- The IF NOT EXISTS clause prevents errors if the user is already created
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT (read-only) privileges on all tables in the hbtn_0d_2 database
-- User can query data but cannot modify, insert, or delete records
-- Backticks protect identifiers from conflicts with reserved words
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`;
