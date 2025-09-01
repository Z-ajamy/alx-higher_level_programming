-- Create a new database named 'hbtn_0d_2'
-- This will fail if the database already exists (no IF NOT EXISTS clause)
CREATE DATABASE hbtn_0d_2;

-- Create a new MySQL user with password authentication
-- User can only connect from localhost (local machine connections only)
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privileges on all tables in the hbtn_0d_2 database to the new user
-- This gives read-only access to the entire database
-- User can query data but cannot modify, insert, or delete records
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`;
