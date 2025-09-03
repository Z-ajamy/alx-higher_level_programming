-- Create a new MySQL user if it doesn't already exist
-- User can only connect from localhost with the specified password
-- Uses double quotes (should work, though single quotes are more standard)
CREATE USER IF NOT EXISTS "user_0d_1"@"localhost" IDENTIFIED BY "user_0d_1_pwd";

-- Attempt to grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO "user_0d_1"@"localhost" WITH GRANT OPTION;

-- Reload MySQL privilege tables to apply changes immediately
FLUSH PRIVILEGES;
