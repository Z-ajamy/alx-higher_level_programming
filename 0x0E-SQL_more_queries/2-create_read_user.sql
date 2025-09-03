-- Create a new database named 'hbtn_0d_2' if it doesn't already exist
-- Safe creation pattern prevents errors on repeated execution
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create a new MySQL user if it doesn't already exist
-- User can only connect from localhost with the specified password
-- Double quotes are acceptable but single quotes are more conventional
CREATE USER IF NOT EXISTS "user_0d_2"@"localhost" IDENTIFIED BY "user_0d_2_pwd";

-- Grant SELECT (read-only) privileges on all tables in the hbtn_0d_2 database
-- User can query data but cannot modify, insert, or delete records
-- This follows the principle of least privilege for security
GRANT SELECT ON hbtn_0d_2.* TO "user_0d_2"@"localhost";
