-- Create the database 'hbtn_0d_2' if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user 'user_0d_2' if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege on the 'hbtn_0d_2' database to the user 'user_0d_2'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Reload the grant tables to ensure that the changes take effect immediately
FLUSH PRIVILEGES;
