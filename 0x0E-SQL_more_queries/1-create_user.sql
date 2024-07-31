-- Create the user 'user_0d_2' connecting from 'localhost' with the specified password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases and tables to the user 'user_0d_2' connecting from 'localhost'
-- and allow the user to grant these privileges to other users
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;

-- Reload the grant tables to ensure that the changes take effect immediately
FLUSH PRIVILEGES;